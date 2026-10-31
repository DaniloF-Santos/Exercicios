import csv
import json
import queue
import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
 
import requests
 
API_URL = "https://fakestoreapi.com/products"
CACHE_FILE = Path(__file__).with_name("produtos_cache.json")
 
TEMAS = {
    "claro": {
        "bg": "#f3f4f6", "painel": "#e5e7eb", "campo": "#ffffff", "zebra": "#f9fafb",
        "fg": "#111827", "fg_suave": "#6b7280",
        "destaque": "#2563eb", "destaque_hover": "#1d4ed8",
    },
    "escuro": {
        "bg": "#111827", "painel": "#1f2937", "campo": "#1f2937", "zebra": "#243041",
        "fg": "#f3f4f6", "fg_suave": "#9ca3af",
        "destaque": "#3b82f6", "destaque_hover": "#60a5fa",
    },
}
 
COLUNAS = {
    "id": ("ID", 50, "center", False),
    "title": ("Título", 430, "w", True),
    "category": ("Categoria", 160, "w", False),
    "price": ("Preço", 90, "e", False),
    "rating": ("Avaliação", 120, "center", False),
}
 
 
def estrelas(nota):
    cheias = round(nota)
    return "★" * cheias + "☆" * (5 - cheias)
 
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Produtos FakeStore")
        self.geometry("1000x560")
        self.minsize(820, 420)
 
        self.tema = "claro"
        self.produtos = []
        self.visiveis = []
        self.por_id = {}
        self.sort_col = None
        self.sort_rev = False
        self.carregando = False
        self.fila = queue.Queue()
 
        self.var_busca = tk.StringVar()
        self.var_cat = tk.StringVar(value="Todas")
        self.var_status = tk.StringVar(value="Pronto")
        self.var_stats = tk.StringVar()
 
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
 
        self._montar_interface()
        self._atalhos()
        self.aplicar_tema()
 
        self.var_busca.trace_add("write", self.filtrar)
        self.after(100, self._checar_fila)
        self.atualizar()
 
    # ------------------------------------------------------------------ UI
    def _montar_interface(self):
        topo = ttk.Frame(self, padding=(12, 12, 12, 6))
        topo.pack(fill="x")
 
        ttk.Label(topo, text="🔎").pack(side="left")
        self.entry_busca = ttk.Entry(topo, textvariable=self.var_busca, font=("Segoe UI", 11))
        self.entry_busca.pack(side="left", fill="x", expand=True, padx=(6, 8))
 
        self.combo_cat = ttk.Combobox(
            topo, textvariable=self.var_cat, values=["Todas"], state="readonly", width=20
        )
        self.combo_cat.pack(side="left", padx=(0, 8))
        self.combo_cat.bind("<<ComboboxSelected>>", self.filtrar)
 
        ttk.Button(topo, text="✖ Limpar", command=self.limpar).pack(side="left", padx=2)
        self.btn_atualizar = ttk.Button(
            topo, text="⟳ Atualizar", style="Accent.TButton", command=self.atualizar
        )
        self.btn_atualizar.pack(side="left", padx=2)
        ttk.Button(topo, text="💾 Exportar", command=self.exportar).pack(side="left", padx=2)
        ttk.Button(topo, text="🌓 Tema", command=self.alternar_tema).pack(side="left", padx=2)
 
        corpo = ttk.Frame(self, padding=(12, 0, 12, 6))
        corpo.pack(fill="both", expand=True)
 
        self.tree = ttk.Treeview(
            corpo, columns=list(COLUNAS), show="headings", selectmode="browse"
        )
        for col, (texto, largura, ancora, estica) in COLUNAS.items():
            self.tree.heading(col, text=texto, command=lambda c=col: self.ordenar(c))
            self.tree.column(col, width=largura, anchor=ancora, stretch=estica)
 
        scroll = ttk.Scrollbar(corpo, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
 
        self.tree.bind("<Double-1>", self.abrir_detalhes)
        self.tree.bind("<Return>", self.abrir_detalhes)
        self.tree.bind("<Button-3>", self._menu_contexto)
        self.tree.bind("<Button-2>", self._menu_contexto)  # macOS
 
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Ver detalhes", command=self.abrir_detalhes)
        self.menu.add_command(label="Copiar título", command=lambda: self._copiar("title"))
        self.menu.add_command(label="Copiar preço", command=lambda: self._copiar("price"))
 
        rodape = ttk.Frame(self)
        rodape.pack(fill="x", side="bottom")
        ttk.Label(rodape, textvariable=self.var_status, style="Status.TLabel").pack(side="left")
        ttk.Label(rodape, textvariable=self.var_stats, style="Status.TLabel").pack(side="right")
 
    def _atalhos(self):
        self.bind("<Control-f>", lambda e: (self.entry_busca.focus_set(), self.entry_busca.select_range(0, "end")))
        self.bind("<Escape>", lambda e: self.limpar())
        self.bind("<F5>", lambda e: self.atualizar())
        self.bind("<Control-e>", lambda e: self.exportar())
 
    def aplicar_tema(self):
        c = TEMAS[self.tema]
        s = self.style
        self.configure(bg=c["bg"])
        s.configure(".", background=c["bg"], foreground=c["fg"], font=("Segoe UI", 10))
        s.configure("TFrame", background=c["bg"])
        s.configure("TLabel", background=c["bg"], foreground=c["fg"])
        s.configure("Suave.TLabel", background=c["bg"], foreground=c["fg_suave"])
        s.configure("Status.TLabel", background=c["painel"], foreground=c["fg_suave"], padding=6)
 
        s.configure("TButton", background=c["painel"], foreground=c["fg"], padding=6, borderwidth=0)
        s.map("TButton",
              background=[("active", c["destaque"]), ("disabled", c["painel"])],
              foreground=[("active", "#ffffff"), ("disabled", c["fg_suave"])])
        s.configure("Accent.TButton", background=c["destaque"], foreground="#ffffff")
        s.map("Accent.TButton",
              background=[("active", c["destaque_hover"]), ("disabled", c["painel"])],
              foreground=[("disabled", c["fg_suave"])])
 
        s.configure("TEntry", fieldbackground=c["campo"], foreground=c["fg"],
                    insertcolor=c["fg"], padding=5, borderwidth=0)
        s.configure("TCombobox", fieldbackground=c["campo"], background=c["painel"],
                    foreground=c["fg"], arrowcolor=c["fg"], padding=4)
        s.map("TCombobox",
              fieldbackground=[("readonly", c["campo"])],
              foreground=[("readonly", c["fg"])])
        self.option_add("*TCombobox*Listbox.background", c["campo"])
        self.option_add("*TCombobox*Listbox.foreground", c["fg"])
        self.option_add("*TCombobox*Listbox.selectBackground", c["destaque"])
 
        s.configure("Treeview", background=c["campo"], fieldbackground=c["campo"],
                    foreground=c["fg"], rowheight=28, borderwidth=0)
        s.map("Treeview",
              background=[("selected", c["destaque"])],
              foreground=[("selected", "#ffffff")])
        s.configure("Treeview.Heading", background=c["painel"], foreground=c["fg"],
                    relief="flat", padding=6, font=("Segoe UI", 10, "bold"))
        s.map("Treeview.Heading", background=[("active", c["destaque"])],
              foreground=[("active", "#ffffff")])
        s.configure("Vertical.TScrollbar", background=c["painel"], troughcolor=c["bg"],
                    arrowcolor=c["fg"], borderwidth=0)
 
        self.tree.tag_configure("par", background=c["campo"])
        self.tree.tag_configure("impar", background=c["zebra"])
        self.menu.configure(bg=c["campo"], fg=c["fg"], activebackground=c["destaque"],
                            activeforeground="#ffffff")
 
    def alternar_tema(self):
        self.tema = "escuro" if self.tema == "claro" else "claro"
        self.aplicar_tema()
 
    # ---------------------------------------------------------- Dados / API
    def atualizar(self):
        if self.carregando:
            return
        self.carregando = True
        self.btn_atualizar.state(["disabled"])
        self.var_status.set("⏳ Carregando produtos...")
        threading.Thread(target=self._baixar, daemon=True).start()
 
    def _baixar(self):
        """Roda em outra thread para a janela não travar."""
        try:
            resp = requests.get(API_URL, timeout=10)
            resp.raise_for_status()
            dados = resp.json()
            CACHE_FILE.write_text(json.dumps(dados, ensure_ascii=False, indent=4), encoding="utf-8")
            self.fila.put(("ok", dados, None))
        except Exception as erro:
            dados = None
            if CACHE_FILE.exists():
                try:
                    dados = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
                except Exception:
                    dados = None
            self.fila.put(("cache" if dados else "erro", dados, str(erro)))
 
    def _checar_fila(self):
        try:
            while True:
                tipo, dados, erro = self.fila.get_nowait()
                self._ao_carregar(tipo, dados, erro)
        except queue.Empty:
            pass
        self.after(100, self._checar_fila)
 
    def _ao_carregar(self, tipo, dados, erro):
        self.carregando = False
        self.btn_atualizar.state(["!disabled"])
 
        if tipo == "erro":
            self.var_status.set("❌ Falha ao carregar")
            messagebox.showerror("Erro", f"Não foi possível buscar os produtos:\n{erro}")
            return
 
        self.produtos = dados
        self.por_id = {p["id"]: p for p in dados}
 
        categorias = sorted({p["category"] for p in dados})
        self.combo_cat.configure(values=["Todas"] + categorias)
        if self.var_cat.get() not in categorias:
            self.var_cat.set("Todas")
 
        self.filtrar()
        hora = datetime.now().strftime("%H:%M:%S")
        if tipo == "ok":
            self.var_status.set(f"✅ Atualizado às {hora}")
        else:
            self.var_status.set(f"📴 Sem conexão, mostrando dados salvos ({hora})")
 
    # ------------------------------------------------- Pesquisa e ordenação
    def filtrar(self, *_):
        termos = self.var_busca.get().lower().split()
        categoria = self.var_cat.get()
 
        resultado = []
        for p in self.produtos:
            if categoria != "Todas" and p["category"] != categoria:
                continue
            texto = f"{p['id']} {p['title']} {p['category']} {p['description']}".lower()
            if all(t in texto for t in termos):
                resultado.append(p)
 
        if self.sort_col:
            resultado.sort(key=self._chave(self.sort_col), reverse=self.sort_rev)
 
        self.visiveis = resultado
        self._preencher()
 
    @staticmethod
    def _chave(col):
        if col == "rating":
            return lambda p: p["rating"]["rate"]
        if col in ("id", "price"):
            return lambda p: p[col]
        return lambda p: str(p[col]).lower()
 
    def ordenar(self, col):
        if self.sort_col == col:
            self.sort_rev = not self.sort_rev
        else:
            self.sort_col, self.sort_rev = col, False
        self._atualizar_cabecalhos()
        self.filtrar()
 
    def _atualizar_cabecalhos(self):
        for col, (texto, *_resto) in COLUNAS.items():
            seta = ""
            if col == self.sort_col:
                seta = "  ▼" if self.sort_rev else "  ▲"
            self.tree.heading(col, text=texto + seta)
 
    def _preencher(self):
        self.tree.delete(*self.tree.get_children())
        for i, p in enumerate(self.visiveis):
            nota = p["rating"]["rate"]
            self.tree.insert(
                "", "end", iid=str(p["id"]),
                values=(
                    p["id"],
                    p["title"],
                    p["category"].title(),
                    f"$ {p['price']:.2f}",
                    f"{estrelas(nota)} {nota}",
                ),
                tags=("par" if i % 2 == 0 else "impar",),
            )
 
        if self.visiveis:
            precos = [p["price"] for p in self.visiveis]
            media = sum(precos) / len(precos)
            self.var_stats.set(
                f"{len(self.visiveis)} de {len(self.produtos)} produtos  |  "
                f"Média ${media:.2f}  |  Menor ${min(precos):.2f}  |  Maior ${max(precos):.2f}"
            )
        else:
            self.var_stats.set("Nenhum produto encontrado")
 
    def limpar(self):
        self.var_busca.set("")
        self.var_cat.set("Todas")
        self.sort_col, self.sort_rev = None, False
        self._atualizar_cabecalhos()
        self.filtrar()
        self.entry_busca.focus_set()
 
    # ------------------------------------------------------------- Extras
    def _produto_selecionado(self):
        sel = self.tree.selection()
        return self.por_id.get(int(sel[0])) if sel else None
 
    def _menu_contexto(self, evento):
        linha = self.tree.identify_row(evento.y)
        if linha:
            self.tree.selection_set(linha)
            self.menu.tk_popup(evento.x_root, evento.y_root)
 
    def _copiar(self, campo):
        p = self._produto_selecionado()
        if not p:
            return
        texto = f"{p['price']:.2f}" if campo == "price" else p[campo]
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.var_status.set(f"📋 Copiado: {texto}")
 
    def abrir_detalhes(self, _evento=None):
        p = self._produto_selecionado()
        if not p:
            return
        c = TEMAS[self.tema]
 
        top = tk.Toplevel(self)
        top.title(f"Produto #{p['id']}")
        top.geometry("520x430")
        top.configure(bg=c["bg"])
        top.transient(self)
        top.bind("<Escape>", lambda e: top.destroy())
 
        quadro = ttk.Frame(top, padding=18)
        quadro.pack(fill="both", expand=True)
 
        ttk.Label(quadro, text=p["title"], font=("Segoe UI", 13, "bold"),
                  wraplength=480, justify="left").pack(anchor="w")
        ttk.Label(quadro, text=f"{p['category'].title()}  •  ID {p['id']}",
                  style="Suave.TLabel").pack(anchor="w", pady=(4, 10))
        ttk.Label(quadro, text=f"$ {p['price']:.2f}", font=("Segoe UI", 22, "bold"),
                  foreground=c["destaque"]).pack(anchor="w")
 
        nota = p["rating"]["rate"]
        ttk.Label(quadro, text=f"{estrelas(nota)}  {nota}  ({p['rating']['count']} avaliações)",
                  style="Suave.TLabel").pack(anchor="w", pady=(2, 10))
 
        caixa = tk.Text(quadro, wrap="word", height=8, relief="flat", bg=c["campo"],
                        fg=c["fg"], font=("Segoe UI", 10), padx=10, pady=10)
        caixa.insert("1.0", p["description"])
        caixa.configure(state="disabled")
        caixa.pack(fill="both", expand=True)
 
        botoes = ttk.Frame(quadro)
        botoes.pack(fill="x", pady=(12, 0))
        ttk.Button(botoes, text="📋 Copiar título", command=lambda: self._copiar("title")).pack(side="left")
        ttk.Button(botoes, text="Fechar", style="Accent.TButton", command=top.destroy).pack(side="right")
 
    def exportar(self):
        if not self.visiveis:
            messagebox.showinfo("Exportar", "Não há produtos na lista para exportar.")
            return
        caminho = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialfile="produtos_filtrados",
            filetypes=[("CSV (Excel)", "*.csv"), ("JSON", "*.json")],
        )
        if not caminho:
            return
 
        if caminho.lower().endswith(".json"):
            Path(caminho).write_text(
                json.dumps(self.visiveis, ensure_ascii=False, indent=4), encoding="utf-8"
            )
        else:
            with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
                w = csv.writer(f, delimiter=";")
                w.writerow(["id", "titulo", "categoria", "preco", "nota", "avaliacoes"])
                for p in self.visiveis:
                    w.writerow([p["id"], p["title"], p["category"], p["price"],
                                p["rating"]["rate"], p["rating"]["count"]])
        self.var_status.set(f"💾 {len(self.visiveis)} produtos exportados")
 
 
if __name__ == "__main__":
    App().mainloop()