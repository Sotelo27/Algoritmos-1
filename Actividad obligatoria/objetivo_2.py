from tkinter import*

def ventana():
	principal=Tk()
	#principal.iconbitmap("icono.ico")
	principal.title("Login Piton")
	principal.geometry("300x130")
	principal.resizable(0,0)
	principal.config(bg="green")
	frame(principal)
	principal.mainloop()

def frame(ventana):
	frame_usuario=Frame(ventana)
	frame_usuario.pack()
    Usuario=Entry(frame_usuario)
    Usuario.place(x=100,y=100)

ventana()

