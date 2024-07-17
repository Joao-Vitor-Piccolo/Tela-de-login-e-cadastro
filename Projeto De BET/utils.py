def limpar(frame_base):
    for widgets in frame_base.winfo_children():
        widgets.destroy()
