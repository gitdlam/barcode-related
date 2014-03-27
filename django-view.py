from django.http import HttpResponse



def index(request):
    return HttpResponse("<b>Put text after the / to get barcode images.  For example http://mel1d23272/f/barcode/123456789.</b>")     


def barcode(request,brcd = ""):
    import code128
    import StringIO
    from base64 import b64encode    
    from PIL import Image, ImageFont, ImageDraw, ImageFilter
#    from winfont import Win32Font

    left_text = brcd
    right_text = ""
    if "::" in brcd:
        right_text = brcd.split("::")[1]

    if right_text != "":
        left_text = brcd.split("::")[0]
        brcd = left_text + "\t" + right_text

    result = ""
    output = StringIO.StringIO()

    code128.code128_image(brcd,height=60, thickness=1).save(output, format="PNG")

    #data = b64encode(open(val + '.png','rb').read())
    data = b64encode(output.getvalue())
    result = '<img  src="data:image/png;base64,{0}">'.format(data)
    output.close()

    result = result + "<br/><br/>"

    output = StringIO.StringIO()
    bc = code128.code128_image(brcd,height=60, thickness=1)
    new_image = Image.new("1", (bc.size[0],bc.size[1] + 30),"white")
    new_image.paste(bc, (0,0,bc.size[0],bc.size[1]))
    draw = ImageDraw.Draw(new_image)
    draw.text((int(bc.size[0] / 2) - int(draw.textsize(left_text,font=ImageFont.truetype("arialbd.ttf", 20))[0]/2), bc.size[1] + 2), left_text, font=ImageFont.truetype("arialbd.ttf", 20))
    del draw
    new_image.save(output, format="PNG")
    data = b64encode(output.getvalue())
    result = result + '<img  src="data:image/png;base64,{0}">'.format(data)
    output.close()



    result = result + "<br/><br/>"

    output = StringIO.StringIO()
    code128.code128_image(brcd,height=100, thickness=2).save(output, format="PNG")
    data = b64encode(output.getvalue())
    result = result + '<img  src="data:image/png;base64,{0}">'.format(data)


    result = result + "<br/><br/>"

    output = StringIO.StringIO()
    bc = code128.code128_image(brcd,height=100, thickness=2)
#    font_image = font.barcode_text_image(30,brcd)
#    f= Win32Font("Arial Bold", 30)
#    font_image = f.renderText(brcd)
    new_image = Image.new("1", (bc.size[0],bc.size[1] + 50),"white")
    new_image.paste(bc, (0,0,bc.size[0],bc.size[1]))
#    new_image.paste(font_image, (0,bc.size[1],font_image.size[0],bc.size[1]+font_image.size[1]))
    font = ImageFont.truetype("arialbd.ttf", 30)
    draw = ImageDraw.Draw(new_image)
    draw.text((int(bc.size[0] / 2) - int(draw.textsize(left_text,font=font)[0]/2), bc.size[1] + 2), left_text, font=font)
    del draw

#    img_resized = new_image.resize((new_image.size[0]/3,new_image.size[1]/3), Image.ANTIALIAS)
#    img_resized.save(output, format="PNG")
    new_image.save(output, format="PNG")
    data = b64encode(output.getvalue())
    result = result + '<img  src="data:image/png;base64,{0}">'.format(data)
    output.close()


    result = result + "<br/><br/>"

    output = StringIO.StringIO()
    code128.code128_image(brcd,height=200, thickness=3).save(output, format="PNG")
    data = b64encode(output.getvalue())
    result = result + '<img  src="data:image/png;base64,{0}">'.format(data)
    output.close()

    result = result + "<br/><br/>"

    output = StringIO.StringIO()
    bc = code128.code128_image(brcd,height=200, thickness=3)
    new_image = Image.new("1", (bc.size[0],bc.size[1] + 50),"white")
    new_image.paste(bc, (0,0,bc.size[0],bc.size[1]))
    font2 = ImageFont.truetype("arialbd.ttf", 36)
    draw = ImageDraw.Draw(new_image)
    draw.text((int(bc.size[0] / 2) - int(draw.textsize(left_text,font=font2)[0]/2), bc.size[1] + 2), left_text, font=font2)
    del draw
    new_image.save(output, format="PNG")
    data = b64encode(output.getvalue())
    result = result + '<img  src="data:image/png;base64,{0}">'.format(data)
    output.close()



    return HttpResponse(result) 
