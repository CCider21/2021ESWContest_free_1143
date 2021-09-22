from UI import UI
from Client import Client


if __name__=="__main__":
		client = Client()
		client.start()
		ui = UI()
		ui.window.mainloop()
