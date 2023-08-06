from PIL import Image

class TextArt:
    def __init__(self, image) -> None:
        self.image = Image.open(image)
        self.w, self.h = self.image.size
        self.ascii_chars = list('01')
        self.ascii_text = ''
        self.ascii_html = ''

    def set_dim(self, width=0, hight=0):
        if width == 0 and hight != 0:
            self.w, self.h = int(self.w/self.h * hight), hight
        elif width != 0 and hight == 0:
            self.w, self.h = width, int(self.h/self.w * width)
        else:
            self.w, self.h = width, hight
        self.image = self.image.resize((self.w, self.h))

    def binary_to_decimal(self, binary):
        decimal = 0
        l = len(binary)
        for x in binary:
            l -= 1
            decimal += pow(2, l) * int(x)
        return int(decimal)

    def span(self, integer, integer_colour):
        return f"<span style='color: rgb{integer_colour};'><b>{integer}</b></span>"
    
    def asciify(self):
        self.ascii_text = ""
        div = 255//(len(self.ascii_chars))
        bwdata = self.image.convert('L').getdata()
        for line_no in range(self.h):
            for pixel in range(line_no*self.w, line_no*self.w + self.w):
                self.ascii_text += self.ascii_chars[bwdata[pixel]//div -1]
    
    def numberify(self, first_char=0):
        for i in self.ascii_chars:
            if not i.isnumeric():
                raise TypeError
        self.asciify()
        if first_char != 0:
            self.ascii_text = str(first_char) + self.ascii_text[1:]
        return self.ascii_text
    
    def primify(self, prime, asis=True, func=bin):
        if not asis and len(bin(int(prime))) == len(func(self.ascii_text)):
            self.ascii_text = func(int(prime))
        elif len(str(int(prime))) == len(self.ascii_text):
            self.ascii_text = str(prime)
        else:
            print("not primified")
    
    def replace(self, text, position):
        self.ascii_text = self.ascii_text[:position]+ text + self.ascii_text[position+len(text):]
    
    def colorify(self):
        color = self.image.getdata()
        if self.ascii_text[:2]=="0b":
            self.ascii_text = self.ascii_text[2:]
        file = '<p style="font-family: monospace;">'
        for line_no in range(self.h):
            for pixel in range(line_no*self.w, line_no*self.w + self.w):
                file += self.span(self.ascii_text[pixel], color[pixel])
            file += '<br>'
        file += "</p>"
        self.ascii_html = file
    
    def ascii_show(self):
        text = ""
        for line_no in range(self.h):
            text += self.ascii_text[line_no*self.w:line_no*self.w + self.w] + "\n"
        print(text)

    def text_output(self, fname):
        text = ""
        for line_no in range(self.h):
            text += self.ascii_text[line_no*self.w:line_no*self.w + self.w] + "\n"
        with open(fname + ".txt", "w") as file:
            file.write(text)
    
    def color_output(self, fname):
        with open(fname + ".html", "w") as file:
            file.write(self.ascii_html)