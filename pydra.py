from cryptography.fernet import Fernet
import wx
import socket
import requests
import socks
import paramiko

# Generar una clave de cifrado y guardarla en un lugar seguro
key = Fernet.generate_key()
f = Fernet(key)

# Función para cifrar la contraseña
def encrypt_password(password):
    return f.encrypt(password.encode()).decode()

# Crear una clase para la ventana principal de la interfaz gráfica de usuario
class PydraFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 400))

        self.panel = wx.Panel(self)

        # Crear etiquetas y cuadros de texto para introducir los datos
        self.password_label = wx.StaticText(self.panel, label="Contraseña:")
        self.password_text = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)

        self.ip_label = wx.StaticText(self.panel, label="Dirección IP:")
        self.ip_text = wx.TextCtrl(self.panel)

        self.port_label = wx.StaticText(self.panel, label="Puerto:")
        self.port_text = wx.TextCtrl(self.panel)

        # Crear botones para cifrar la contraseña y realizar las diferentes tareas
        self.encrypt_button = wx.Button(self.panel, label="Cifrar contraseña")
        self.Bind(wx.EVT_BUTTON, self.onEncrypt, self.encrypt_button)

        self.scan_button = wx.Button(self.panel, label="Escaneo de puertos")
        self.Bind(wx.EVT_BUTTON, self.onPortScan, self.scan_button)

        self.brute_force_button = wx.Button(self.panel, label="Ataque de fuerza bruta")
        self.Bind(wx.EVT_BUTTON, self.onBruteForce, self.brute_force_button)

        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Crear un sizer para organizar los widgets en la ventana
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.password_label, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.password_text, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.encrypt_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.sizer.Add(self.ip_label, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.ip_text, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.port_label, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.port_text, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.scan_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.sizer.Add(self.brute_force_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 10)

        self.panel.SetSizer(self.sizer)
        self.sizer.Fit(self)

    def onEncrypt(self, event):
        # Obtener la contraseña ingresada por el usuario
        password = self.password_text.GetValue()

        # Cifrar la contraseña y mostrar el resultado en el cuadro de texto
        encrypted_password = encrypt_password(password)
        self.text_ctrl.AppendText(f"Contraseña cifrada: {encrypted_password}\n")

    def onPortScan(self, event):
        # Obtener la dirección IP y el puerto ingresados por el usuario
        ip = self.ip_text.GetValue()
        port = int(self.port_text.GetValue())

        # Realizar el escaneo de puertos y mostrar los resultados en el cuadro de texto
        open_ports = self.scan_ports(ip, port)
        self.text_ctrl.AppendText(f"Puertos abiertos en {ip}: {open_ports}\n")

    def scan_ports(self, ip, port):
        # Función para realizar el escaneo de puertos
        open_ports = []

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except Exception as e:
            pass

        return open_ports

    def onBruteForce(self, event):
        # Obtener la dirección IP y la contraseña ingresados por el usuario
        ip = self.ip_text.GetValue()
        password = self.password_text.GetValue()

        # Realizar el ataque de fuerza bruta y mostrar los resultados en el cuadro de texto
        result = self.brute_force_attack(ip, password)
        self.text_ctrl.AppendText(result)

    def brute_force_attack(self, ip, password):
        # Función para realizar el ataque de fuerza bruta a través de SSH
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username='root', password=password, timeout=5)
            client.close()
            return f"¡Ataque de fuerza bruta exitoso! Contraseña: {password}\n"
        except paramiko.AuthenticationException:
            return f"Contraseña incorrecta: {password}\n"
        except Exception as e:
            return f"Error al realizar el ataque de fuerza bruta: {e}\n"

class PydraApp(wx.App):
    def OnInit(self):
        frame = PydraFrame(None, title="Pydra")
        frame.Show()
        return True

if __name__ == "__main__":
    app = PydraApp()
    app.MainLoop()
