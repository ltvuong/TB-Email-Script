import yagmail, csv

# Information about sender email
senderAddress = ""
password = ""

yagmail.register(senderAddress, password)

# Links to tutor resources
vGuideurl = "https://docs.google.com/document/d/1fdgeUaYrOvOmyaGiro_KEb0_1qV78CFPg8ryd9VN9HU/edit"
gGuideurl = "https://drive.google.com/drive/folders/1BdeKEOyVppVMdtOdD7j3ThKJBZdNxaqV?usp=sharing"
tResources = "https://drive.google.com/drive/folders/1p7hMpNckBvkD8gGJ1jDrAw8kmEY_qSW0"

# Email images
botBanner = "https://ci5.googleusercontent.com/proxy/jfdrc3ymX7v8Af3amdVT0t2ZQ5QOHiMQxpIhUVslXDYccpqyN9DtEdcdKHZdB3V4zrXnnkm34L7k5bSazGszvSFQlqMka_IDbixgfsv7jIQTjfg2WVVVXpft8NhvQSz5krCILBJmVxmK27RZiVlux2XYHtMhPiI2TvIJV7NMheOLkjStXveROGm2ULjibh3Fgrpqt2pqSpt_4BaJDQ=s0-d-e1-ft#https://docs.google.com/uc?export=download&id=1fe4IaroGC4Eq_GKaznPuBvOzsgMk-Az4&revid=0B9bKrXoLLd0aZ1VrOTZRUno1RlNDWjhsSmxJMlNIMUMrQ1IwPQ"

# Loading CSV with email variables
with open("data.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for session, headtutor_email, headtutor_name, v_email, v_name, ct_name, ct_grade, ct_college, ct_email, ct_phone, subject, grade, p1_student, p1_desc, p1_name, p1_lang, p1_email, p1_phone, p1_text, p2_student, p2_desc, p2_name, p2_lang, p2_email, p2_phone, p2_text, p3_student, p3_desc, p3_name, p3_lang, p3_email, p3_phone, p3_text, p4_student, p4_desc, p4_name, p4_lang, p4_email, p4_phone, p4_text, p5_student, p5_desc, p5_name, p5_lang, p5_email, p5_phone, p5_text in reader:

        # Email subject line
        subjectLine = "Tutor Assignment! (" + session + ")"

        # Generates student description texts
        # Code uses the p_text value to see if there is a student based
        # on whether or not p_text exists i.e has the word "is" in it
        # Then the code generates a blurb and attaches it to the 'studinfo' variable
        studinfo = ""
        if "is" in p1_text:
            studinfo = studinfo + ("""<span style="font-size:15px;"><b>""" +str(p1_student)+ """</b></span>
            """ +str(p1_desc)+ """
            <span style="color:#cf2714;"><b>Parent name:</b> """ +str(p1_name)+ """
            <b>Language Preference:</b> """ +str(p1_lang)+ """
            <b>Phone number:</b> """ +str(p1_phone)+ """
            <b>Text preference:</b> """ +str(p1_text)+ """
            <b>Parent email:</b> """ +str(p1_email)+ """</span>
            """)
        if "is" in p2_text:
            studinfo = studinfo + ("""
            <span style="font-size:15px;"><b>""" + str(p2_student) + """</b></span>
            """ + str(p2_desc) + """
            <span style="color:#cf2714;"><b>Parent name:</b> """ + str(p2_name) + """
            <b>Language Preference:</b> """ +str(p2_lang)+ """
            <b>Phone number:</b> """ + str(p2_phone) + """
            <b>Text preference:</b> """ + str(p2_text) + """
            <b>Parent email:</b> """ + str(p2_email) + """</span>
            """)
        if "is" in p3_text:
            studinfo = studinfo + ("""
            <span style="font-size:15px;"><b>""" +str(p3_student)+ """</b></span>
            """ +str(p3_desc)+ """
            <span style="color:#cf2714;"><b>Parent name:</b> """ +str(p3_name)+ """
            <b>Language Preference:</b> """ +str(p3_lang)+ """
            <b>Phone number:</b> """ +str(p3_phone)+ """
            <b>Text preference:</b> """ +str(p3_text)+ """
            <b>Parent email:</b> """ +str(p3_email)+ """</span>
            """)
        if "is" in p4_text:
            studinfo = studinfo + ("""
            <span style="font-size:15px;"><b>""" +str(p4_student)+ """</b></span>
            """ +str(p4_desc)+ """
            <span style="color:#cf2714;"><b>Parent name:</b> """ +str(p4_name)+ """
            <b>Language Preference:</b> """ +str(p4_lang)+ """
            <b>Phone number:</b> """ +str(p4_phone)+ """
            <b>Text preference:</b> """ +str(p4_text)+ """
            <b>Parent email:</b> """ +str(p4_email)+ """</span>
            """)
        if "is" in p5_text:
            studinfo = studinfo + ("""
            <span style="font-size:15px;"><b>""" +str(p5_student)+ """</b></span>
            """ +str(p5_desc)+ """
            <span style="color:#cf2714;"><b>Parent name:</b> """ +str(p5_name)+ """
            <b>Language Preference:</b> """ +str(p5_lang)+ """
            <b>Phone number:</b> """ +str(p5_phone)+ """
            <b>Text preference:</b> """ +str(p5_text)+ """
            <b>Parent email:</b> """ +str(p5_email)+ """</span>
            """)

        # Code to generate body of the email in HTML format
        body = """\
        <html style="font-family:arial;">
            <head>Hi <span style="font-size:15px;"><b>""" +str(v_name)+ """</b></span>,</head>
            <body>
                First of all, thank you so much for volunteering your time to help out with Teaching Buddies in Times of Crisis! We really appreciate your time and patience as we have been figuring out our program! 
                We have started getting sign ups from parents and you have been selected to teach these first cohort of students for the """ +str(session)+ """ session!
                
                Each tutor will have another tutor pair and your partner is <b>""" +str(ct_name)+ """</b>. They're a <b>""" +str(ct_grade)+ """</b> at <b>""" +str(ct_college)+ """</b>. Here is their email address: <b>""" +str(ct_email)+ """</b> and their phone number: <b>""" +str(ct_phone)+ """</b>.
                
                One of the things we want you to do first is to contact your fellow tutor and lesson plan for these students! If you need any help with that, please refer to the <b><a href=""" +str(vGuideurl)+ """>volunteer guide</a></b> (broad overview) or to the <b><a href=""" +str(gGuideurl)+ """>grade guide</a></b> (slightly more specific guide based on grade level groups).

                These are the <b>""" +str(grade)+ """ grade</b> students that you will be tutoring in <b>""" +str(subject)+ """</b> and a little bit about them:
            
                <blockquote>""" +str(studinfo)+ """</blockquote>
                You will be planning a lesson time every week with the parents of these students. If you are not able to tutor anymore or would like to drop out, please let us know immediately. Since we are not running background checks, it is highly imperative that <b>BOTH</b> of you are there.  

                We would like for you to introduce yourselves, schedule a time with them for tutoring sessions, and confirm what kind of resources they have (access to printer, library, paper, pen, etc.). If you need any help with that process, we do have a folder linked <b><a href=""" +str(tResources)+ """>here</a></b> that has some helpful templates and guides that will make this process easier.
                 
                <b>TLDR:</b>
                1. Contact your co-tutor and introduce yourself to them. Possibly do some initial lesson planning with them.
                2. Contact the parents and introduce yourselves to them.
                3. Decide on a time that works best for all of you every week.
                4. Final lesson planning with co-tutor.
                5. Have your first session
                 
                Again, thank you so much for agreeing to volunteer with us! We hope that you have a fulfilling and fun experience with them. If you have any questions or problems please feel free to email us at <b>teachingbuddies2020@gmail.com</b> or your assigned head tutor, <b>""" +str(headtutor_name)+ """</b>, at <b>""" +str(headtutor_email)+ """</b>.
                 
                Best,
                 
                Teaching Buddies Leadership :)
                
                <footer><img src=""" +str(botBanner)+ """ width="25%" height="25%"></footer>
            </body>
        </html>
        """

        # This is what sends the email using Yagmail package
        receiver = v_email
        yag = yagmail.SMTP(senderAddress)
        yag.send(
            to=receiver,
            subject=subjectLine,
            contents=body,
            cc=headtutor_email,
            bcc=senderAddress,
        )

        # Email confirmation
        print("Email successfully sent to:", receiver)