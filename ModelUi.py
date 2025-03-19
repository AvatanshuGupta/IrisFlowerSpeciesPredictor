import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tkinter import *
from PIL import Image,ImageTk

#Getting Data
d=pd.read_csv('Iris.csv')
df=d.drop(columns=['Id'])

#Transforming Data in Species column using LabelEncoder
le=LabelEncoder()
df['Species']=le.fit_transform(df['Species'])

#Preparing Data for model training
x=df.drop(columns=['Species'])
y=df['Species'] 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=40)

#Training a Logistic Regression Model
model=LogisticRegression()
model.fit(x_train,y_train)
#print(model.score(x_test,y_test)*100)

#Making UI
root=Tk()
root.geometry('1100x920')
root.title('IRIS FLOWER SPECIES PREDICTOR')




#background image
bg=Image.open('ImageResources/background.jpg')
bg=bg.resize((1100,920),Image.LANCZOS)
bg_image=ImageTk.PhotoImage(bg)
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)



#getting images of flower
Iris_setosa=Image.open('ImageResources/Iris-setosa.jpg')
Iris_viginica=Image.open('ImageResources/iris virginica.jpg')
Iris_versicolor=Image.open('ImageResources/Iris-versicolor.jpg')






#Welcome Text
Text=Label(text='Welcome To Iris Flower Species Predictor',font=('Arial',30,'bold'))
Text.pack(pady=30,ipadx=2,ipady=2)

#Button Action
def action():
 try:
  isl=float(sl.get())
  isw=float(sw.get())
  ipl=float(pl.get())
  ipw=float(pw.get())
  feature_names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
  ar = pd.DataFrame([[isl,isw,ipl,ipw]], columns=feature_names)
  pred=model.predict(ar)
  if pred[0] == 0:
            species_image = ImageTk.PhotoImage(Iris_setosa)
            species_name = "Iris Setosa"
  elif pred[0] == 1:
            species_image = ImageTk.PhotoImage(Iris_versicolor)
            species_name = "Iris Versicolor"
  elif pred[0] == 2:
            species_image = ImageTk.PhotoImage(Iris_viginica)
            species_name = "Iris Virginica"

  result_label = Label(root, text="", font=("Arial", 20, "bold"))
  result_label.pack(pady=10)
      
  result_label.config(image=species_image, text=species_name, compound='top')
  result_label.image = species_image
 
 except:
  print("Enter Values In Correct Format")
   

#Getting Data from User
textsl=Label(text='Enter Sepal Length',font='Orbitron,10')
textsl.pack()
sl=Entry(root,font='20')
sl.pack(ipadx=5,ipady=2,pady=7,padx=20)

textsw=Label(text='Enter Sepal Width',font='Orbitron,10')
textsw.pack()
sw=Entry(root,font='20')
sw.pack(ipadx=5,ipady=2,pady=7,padx=20)

textpl=Label(text='Enter Petal Length',font='Orbitron,10')
textpl.pack()
pl=Entry(root,font='20')
pl.pack(ipadx=5,ipady=2,pady=7,padx=20)

textpw=Label(text='Enter Petal Width',font='Orbitron,10')
textpw.pack()
pw=Entry(root,font='20')
pw.pack(ipadx=5,ipady=2,pady=7,padx=20)


#Setting up Button
get=Button(text='Get Prediction',command=action,font=('30'))
get.pack(pady=10)



root.mainloop()
