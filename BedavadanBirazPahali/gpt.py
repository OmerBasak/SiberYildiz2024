from tkinter import Tk, Label

chars = ['0x73', '0x32', '0x64', '0x36', '0x76', '0x34', '0x7f', '0x38', '0x74', '0x6d', '0x3b', '0x85', '0x3b', '0x82', '0x81', '0x3f', '0x7d', '0x40', '0x78', '0x7f', '0x75', '0x7c', '0x44', '0x8b', '0x90', '0x8d']
flash_text = ''.join(chr(int(c, 16) - i) for i, c in enumerate(chars))

root = Tk()
root.title('Flash Message')

flash_label = Label(root, text=flash_text, fg='#F00', font=('bold', 50), bg='#000', padx=3, pady=3, width=300, height=50)
flash_label.pack()

root.mainloop()