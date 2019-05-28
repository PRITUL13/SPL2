
############
from PIL import Image
import mysql.connector
infile = 'C:/Users/Priyotuli/Desktop/pl/spl.png.'
chopsize = 64

img = Image.open(infile)
width, height = img.size
#print(infile)

class parts():
    # Save Chops of original image


    def __init__(self):
        "do "
    def run(self):
        i=int(0)
        mydb = mysql.connector.connect(
                      host="localhost",
                      user="saiba",
                      passwd="1110235361",
                      database="priotuli"
          )
        for x0 in range(0, width, 64):

            for y0 in range(0, height,64):
              mycursor = mydb.cursor()
              box = (x0, y0,
                     x0+chopsize if x0+chopsize <  width else  width - 1,
                     y0+chopsize if y0+chopsize < height else height - 1)

              #print('%s %s' % (infile, box))
              print("running")
              img.crop(box).save('%s.%d.jpg' % (infile.replace('.jpg',''), i))
              fileName=str(infile+str(i)+".jpg")
              print(fileName)
              sql="insert into arts(art_name) values(%s)"
              val=(fileName,)
              mycursor.execute(sql,val)
              mydb.commit()
              mycursor.close()
              i+=1
        mydb.close()

              ################
parts().run()
