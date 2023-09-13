from utilities.mail.outlook.read import Read
from utilities.excel.range.write_range import WriteRange
from utilities.excel.range.read_range import ReadRange
import openpyxl as xl
from utilities.excel.util.utils import ExcelWorkbook
from utilities.excel.range.get_range import GetRange
import logging,re
# temp_folder = "C:\\Users\\usuario\\Desktop\\Temp"
# folder = "C:\\Users\\usuario\\Desktop\\OutlookMails"
# clients = {
#     "Pacasmayo":"Gestión Pacasmayo",
#     "Kallpa":"Gestión Kallpa",
#     "Lima Expresa":"Gestión Lima Expresa",
#     "Samay":"Gestión Samay",
#     "Aguaytia":"Gestión Aguaytia"}
# client_folder = list(clients.keys())
# mail_account = list(clients.values())
# mail_folder = "Bandeja del Bot"
# data = Read.read_data(mail_account,mail_folder,client_folder,folder,temp_folder)
# print(data)
# ticket = "TK ########"
# req = "Requerimiento"
# path = r"C:\Users\usuario\Desktop\prueba.xlsx"
# sheet = "Sheet"
# cell = "A1"
# range = "A1:O5"
# data = [['Pacasmayo', 'A64ED557DE12438580AE1F43F62AAFD0', 'ZPAC', 'SD', 'SD', 'IN', 'BAJA', '110001', 'Gestión Pacasmayo', None, None, None, None, None, 'OK', None], ['Kallpa', 'B2ADFB85F0B14A5585F128CE49442B51', 'Kallpa', 'SD', 'SD', 'IN', 'BAJA', '110001', 'Gestión Kallpa', None, None, None, None, None, 'OK', None], ['Lima Expresa', '39052437604343BC92E453948C57F678', 'Limex', 'SD-MM', 'SD', 'IN', 'BAJA', '110001', 'Gestión Lima Expresa', None, None, None, None, None, 'OK', None], ['Samay', '37548705D9CE4C1685C7A396D858A2C3', 'Samay', 'SD', 'SD', 'IN', 'BAJA', '110001', 'Gestión Samay', None, None, None, None, None, 'OK', None], ['Aguaytia', '22E1EE60627C4826950D1D7B05D67325', 'Aguaytia', 'SD-MM', 'SD', 'IN', 'BAJA', '110001', 'Gestión Aguaytia', None, None, None, None, None, 'OK', None]]
# print(data.values.tolist())
# #WriteRange.write_range(path,sheet,cell,data)
# data_read=ReadRange.read_range(path,sheet,range)
# print(data_read)
# data = [['Aguaytia', '57D1E159EDC74B58827EEF32475C0D34', 'Aguaytia', 'SD-MM', 'SD', 'IN', 'BAJA', '110002', 'Gestión Aguaytia', None, None, None, None, None, 'OK', None]]
# for data_list in data:
#     subject_init = Read.subject_reply_message(data_list,ticket,req)
#     Read.reply_mails(clients[data_list[0]],mail_folder,data_list[1],subject_init)
#     print(subject_init)
from PIL import Image
import glob

# Create the frames
frames = []
duration_frame = []
time = 1000
imgs = glob.glob("C:\\ipa_log\\100\\*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    duration_frame.append(time)
duration_frame[-1] = 3*time
# Save into a GIF file that loops forever
frames[0].save('C:\\ipa_log\\100\\png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=duration_frame, loop=0)
