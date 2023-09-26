from nicegui import app,ui
import subprocess

canrun = True

def button_Iniciar_on_click():
    global canrun
    if canrun:
        canrun = False
        ui.notify('Rodando...', position="top")
        with ui.row().classes('w-full justify-center'):
            ui.spinner('audio', size='lg', color='green')
        subprocess.Popen([r"assets\app\malware_detector.exe"], shell=True, startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW))

def main():
    with ui.row().classes('w-full justify-center'):
        ui.image("assets/img/logo.png").classes('text-center w-1/2')
        ui.label("Detectar Ransomware").classes('text-center w-1/2 text-3xl')
        ui.button("Iniciar", on_click=lambda: button_Iniciar_on_click()).classes('bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full text-center w-1/2')

app.native.window_args['resizable'] = False
if __name__ in ["__mp_main__","__main__"]:
    main()
    ui_ = ui.run(native=True, window_size=(800, 620), fullscreen=False, title="Cute Guard", reload=False)