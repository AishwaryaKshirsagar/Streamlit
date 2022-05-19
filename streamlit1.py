import streamlit as st
# from PIL import Image
from textblob import TextBlob
# from multiapp import MultiApp
# from apps import home, data, model # import your app modules here

# app = MultiApp()

# # Add all your application here
# app.add_app("Home", home.app)
# app.add_app("Data", data.app)
# app.add_app("Model", model.app)
# The main app

container = st.container()

st.title("Mood Based Recommendation system")

# image = Image.open('Three.jpg')
# st.image(image, caption=' ',width = 520)

html_temp = '<div class="img1">
           <img src="https://melodica.ae/wp-content/uploads/2017/11/girl_with_headphones_music_m-min.jpg" alt="img"> 

           <img src="https://ehonami.blob.core.windows.net/media2020/2021/02/GettyImages-1204482432-1024x683.jpg" alt="img2">
        </div>'
st.markdown(html_temp, unsafe_allow_html = True)

title = '<p style="font-family:Sans-serif; color:Pink; font-size: 20px;">Certain Events can make you feel sad, anxious, surprised, excited or shocked. You can still make yourself feel better by watching a movie which would relax you, listening to songs which may calm you down or maybe read an adventure book!!</p>'
st.markdown(title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:White; font-size: 20px;">Don\'t worry, we are here to help you feel better</p>'
st.markdown(title, unsafe_allow_html=True)

# image = Image.open('/scale.jpg')
# st.image(image, caption=' ',width = 620)

title = '<p style="font-family:Courier; color:cyan; font-size: 30px;">Just Answer the below questions to get recommendations based on your current mood</p>'
st.markdown(title, unsafe_allow_html=True)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">1.when was the last time you where really happy?: </p>'
st.markdown(question, unsafe_allow_html=True)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = i dont remember      2 = few months ago      3 = few weeks ago    4 = few days ago    5 = few moments ago</p>'
st.markdown(title, unsafe_allow_html=True)
q1 = st.slider('Select a value between 1 to 5:  ',min_value=1, max_value = 5,step =1, key = 1)
st.write(q1)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">2.overall how do u rate your comfortness around people?: </p>'
st.markdown(question, unsafe_allow_html=True)
q2 = st.slider("Select a value between 1 to 5:  ",min_value=1, max_value = 5,step =1, key=2)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">low = (1) and high = (5)</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q2)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">3.Rate how often u face problems in your work/studies?: </p>'
st.markdown(question, unsafe_allow_html=True)
q3 = st.slider("Select a value between 1 to 5:  ",min_value=1, max_value = 5,step =1, key=3)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = always      2 = very often      3 = sometimes    4 = not much    5 = no</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q3)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">4.Rate how often you feel angry/irritated?: </p>'
st.markdown(question, unsafe_allow_html=True)
q4 = st.slider("Select a value between 1 to 5: ",min_value=1, max_value = 5,step =1, key=4)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = always      2 = very often      3 = sometimes    4 = not much    5 = no</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q4)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">5.when was the last time you felt good about your self?: </p>'
st.markdown(question, unsafe_allow_html=True)
q5 = st.slider("Select a value between 1 to 5: ",min_value=1, max_value = 5,step =1, key=5)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = i dont remember      2 = few months ago      3 = few weeks ago    4 = few days ago    5 = few moments ago</p>'
st.markdown(title, unsafe_allow_html=True) 
st.write(q5)

text_area = '<p style="font-family:Courier; color:Pink; font-size: 25px;">How was your day? Please describe in 20 words. You can describe about the various events that took place today. </p>'
st.markdown(text_area, unsafe_allow_html=True)

text_area = st.text_area("Start Typing here - ")
blob = TextBlob(text_area)
sentiment = blob.sentiment.polarity

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">6.Rate how often u face problems in your work/studies?  </p>'
st.markdown(question, unsafe_allow_html=True)
q6 = st.slider("Select a value between 1 to 5: ",min_value=1, max_value = 5,step =1,key=6)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = always      2 = very often      3 = sometimes    4 = not much    5 = no</p>'
st.markdown(title, unsafe_allow_html=True) 
st.write(q6)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">7.how much do u overthink?  </p>'
st.markdown(question, unsafe_allow_html=True)
q7 = st.slider("Select a value between 1 to 5: ",min_value=1, max_value = 5,step =1,key=7)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = always      2 = very often      3 = sometimes    4 = not much    5 = no</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q7)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">8.how content/happy you are with your relationship and family? </p>'
st.markdown(question, unsafe_allow_html=True)
q8 = st.slider("Select a value between 1 to 5: ",min_value=1, max_value = 5,step =1,key=8)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = never      2 = not much      3 = sometimes    4 = very often    5 = always</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q8)    

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">9.how often do you feel anxious/awkward around people?  </p>'
st.markdown(question, unsafe_allow_html=True)
q9 = st.slider("Select a value between 1 to 5:  ",min_value=1, max_value = 5,step =1,key=9)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = always      2 = very often      3 = sometimes    4 = not much    5 = no</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q9)

question = '<p style="font-family:Courier; color:Orange; font-size: 25px;">10.how often you feel like sharing things with people?  </p>'
st.markdown(question, unsafe_allow_html=True)
q10 = st.slider("Select a value between 1 to 5:  ",min_value=1, max_value = 5,step =1,key=10)
title = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">1 = never      2 = not much      3 = sometimes    4 = very often    5 = always</p>'
st.markdown(title, unsafe_allow_html=True)
st.write(q10)

count = q1+q2+q3+q4+q5+q6+q7+q8+q9+q10
print(count)
print(sentiment)

if(sentiment!=0):
    if(count > 35 and sentiment > 0.3):
        # ans = '<p style="font-family:Courier; color:cyan; font-size: 40px;">Select Selection2 from sidebar menu to get your recommendations!  </p>'
        # st.markdown(ans, unsafe_allow_html=True)

#         image = Image.open('/happy.jpg')
#         st.image(image, caption=' ',width = 550)
        st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
        st.write("List of books:\n 1. The panic years.\n 2. Carry on Jeeves\n 3. That moment when.\n 4. Bon Mortimer\n 5. The Idiot\n 6. The Timewaster letters.\n 7. The happiest project \n . 8. The Art of happiness \n . 9. The Wangs\n 10. How to be Normal")
        st.write("List of movies:\n 1. Liar Liar \n 2. Inside out \n 3. Men in black \n 4. Housefull\n 5. Good Boys\n 6. Welcome.\n 7. Klown\n 8. Phir Hera Pheri\n 9. Khichadi\n 10.Dhamaal")
        st.write("List of songs: \n 1. Bruno Mars \n 2. Maroon 5 \n 3. Justin Beiber\n 4. Taylor Swift\n 5. Beatles\n 6. Britney Sphears\n 7. Jennifer Lopes\n 8. Kelly Clarkson\n 9. Dua lipa\n 10. Shawn Mendes")



    if(count < 15 and count!=0 and sentiment < -0.3):
        ans = '<p style="font-family:Courier; color:cayn; font-size: 40px;">Select Selection3 from sidebar menu to get your recommendations!  </p>'
        st.markdown(ans, unsafe_allow_html=True)
#         image = Image.open('/change.jpg')
#         st.image(image, caption=' ',width = 450)
        st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
        st.subheader("List of books:\n 1. How to stay happy \n 2. When life gives you lemons \n 3. How to become a people magnet\n 4. The Aspirant\n 5. Ikigai\n 6. Being an Indian Teenager\n 7. Before the coffee gets cold\n 8. Fear Not Be strong\n 9. Better than best friends.\n 10. You only live once.")
        st.subheader("List of movies:\n 1. Marley and me \n 2. Harry potter \n 3. The pursuit of happiness\n 4. Legally Blond\n 5. Little miss sunshine\n 6. Pitch Perfect\n 7. The Princess Diaries\n 8. The Shawshank Redemption\n 9. La La Land\n 10. Clueless")
        st.subheader("List of songs:\n 1. Stronger \n 2. Titanium \n 3. Fight song\n 4. Yun hi chala chal\n 5. Hall of Fame\n 6. Roar\n 7. Jeete hain chal\n 8. Phir se ud chala\n 9. Chak de india\n 10. Roobaroo")


    if(15 < count < 35 and -0.3 < sentiment < 0.3):
        ans = '<p style="font-family:Courier; color:cyan; font-size: 40px;">Select Selection4 from sidebar menu to get your recommendations!  </p>'
        st.markdown(ans, unsafe_allow_html=True)
#         image = Image.open('/Behappy.jpg')
#         st.image(image, caption=' ',width = 450)
        st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
        st.subheader("List of books:\n 1. Hardy boys \n 2. Harry potter \n 3. Percy Jackson\n 4. Famous Five\n 5. Secret seven\n 6. Mahabharata Secret\n 7. The girl on the train\n 8. Da vinci code\n 9. The sands of time\n 10. Angels and demons")
        st.subheader("List of movies:\n 1. Angels and demons \n 2. Justice League \n 3. Spiderman\n 4. Avengers\n 5. Batman\n 6. Martian\n 7. Da vinci code\n 8. Gravity\n 9. Interstellar\n 10. Fast and furious")
        st.subheader("List of songs:\n 1. Cold play \n 2. Kesha \n 3. Beatles\n 4. Arijit singh\n 5. A R Rahman\n 6. Atif Aslam\n 7. Pitbull\n 8. Drake\n 9. OneRepublic\n 10. Charlie Puth")


def main():
    
    st.markdown("""
    # Mood Recommendation system
    """)



    #Selection2 = happy
    #Selectin3 = sad
    # selection4 = normal

    

    # if choice =="Home":
    #     # st.subheader("Home")
    #    pass

    # elif choice == "Selection2":
#         image = Image.open('/happy.jpg')
#         st.image(image, caption=' ',width = 550)
    #     st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
    #     st.write("List of books:\n 1. The panic years.\n 2. Carry on Jeeves\n 3. That moment when.\n 4. Bon Mortimer\n 5. The Idiot\n 6. The Timewaster letters.\n 7. The happiest project \n . 8. The Art of happiness \n . 9. The Wangs\n 10. How to be Normal")
    #     st.write("List of movies:\n 1. Liar Liar \n 2. Inside out \n 3. Men in black \n 4. Housefull\n 5. Good Boys\n 6. Welcome.\n 7. Klown\n 8. Phir Hera Pheri\n 9. Khichadi\n 10.Dhamaal")
    #     st.write("List of songs: \n 1. Bruno Mars \n 2. Maroon 5 \n 3. Justin Beiber\n 4. Taylor Swift\n 5. Beatles\n 6. Britney Sphears\n 7. Jennifer Lopes\n 8. Kelly Clarkson\n 9. Dua lipa\n 10. Shawn Mendes")

    # elif choice == "Selection3":
    #     image = Image.open('/change.jpg')
    #     st.image(image, caption=' ',width = 450)
    #     st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
    #     st.subheader("List of books:\n 1. How to stay happy \n 2. When life gives you lemons \n 3. How to become a people magnet\n 4. The Aspirant\n 5. Ikigai\n 6. Being an Indian Teenager\n 7. Before the coffee gets cold\n 8. Fear Not Be strong\n 9. Better than best friends.\n 10. You only live once.")
    #     st.subheader("List of movies:\n 1. Marley and me \n 2. Harry potter \n 3. The pursuit of happiness\n 4. Legally Blond\n 5. Little miss sunshine\n 6. Pitch Perfect\n 7. The Princess Diaries\n 8. The Shawshank Redemption\n 9. La La Land\n 10. Clueless")
    #     st.subheader("List of songs:\n 1. Stronger \n 2. Titanium \n 3. Fight song\n 4. Yun hi chala chal\n 5. Hall of Fame\n 6. Roar\n 7. Jeete hain chal\n 8. Phir se ud chala\n 9. Chak de india\n 10. Roobaroo")

    # elif choice == "Selection4":
    #     image = Image.open('/Behappy.jpg')
    #     st.image(image, caption=' ',width = 450)
    #     st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
    #     st.subheader("List of books:\n 1. Hardy boys \n 2. Harry potter \n 3. Percy Jackson\n 4. Famous Five\n 5. Secret seven\n 6. Mahabharata Secret\n 7. The girl on the train\n 8. Da vinci code\n 9. The sands of time\n 10. Angels and demons")
    #     st.subheader("List of movies:\n 1. Angels and demons \n 2. Justice League \n 3. Spiderman\n 4. Avengers\n 5. Batman\n 6. Martian\n 7. Da vinci code\n 8. Gravity\n 9. Interstellar\n 10. Fast and furious")
    #     st.subheader("List of songs:\n 1. Cold play \n 2. Kesha \n 3. Beatles\n 4. Arijit singh\n 5. A R Rahman\n 6. Atif Aslam\n 7. Pitbull\n 8. Drake\n 9. OneRepublic\n 10. Charlie Puth")

if __name__ == '__main__':
    main()

