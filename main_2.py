from tkinter import *
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
print("\nHello, this is a carrerguidance chat bot which will help you in enhancing your carrer, only if you are in 9th, 10th, or 12th!")

name_input = input("\nWhat is your name?: ")

print(f"\nHello {name_input}!")

grade_input = int(input("\nWhat grade are you in?: "))

if grade_input == 9 or grade_input == 10 or grade_input == 12:
    print("\nOkay let's start")
else:
    print("\nSorry, sadly we do not support any other grades except 9, 10, 12 :(\n")
    
print("\nThere are currently 6 Voacational Subjects supported by us, these are: \n(1) Information Technology 402 \n(2) Artificial Intelligence 417 \n(3) Beauty & Wellness 407 \n(4) Travel And Tourism 406 \n(5) Health Care 413 \n(6) Financial Management 405")

print("\nNOTE --> Remember, whichever subject you take in 9th standard will continue in 10th standard")

voc_sub_input = int(input("\nJust enter the 3 Digit code written next to the name of the subject for which you want to know about: "))


class InformationTechnology:
    if voc_sub_input == 402:
        print("\nInformation Technology (IT) is a business sector that deals with computing, including hardware, software, telecommunications and generally anything \ninvolved in the transmittal of information or the systems that faciliate communication. IT also includes the management of data.\n")   
    def it():
        print("\nInformation Technology (IT) is a business sector that deals with computing, including hardware, software, telecommunications and generally anything \ninvolved in the transmittal of information or the systems that faciliate communication. IT also includes the management of data.\n")

class ArtificialIntelligence:
    if voc_sub_input == 417:
        print("\nArtificial intelligence is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision.\n") 
    def ai():
        print("\nArtificial intelligence is the simulation of human intelligence processes by machines, especially computer systems. Specific applications of AI include expert systems, natural language processing, speech recognition and machine vision.\n")

class BeautyAndWellness:
    if voc_sub_input == 407:
        print("\nThe outward appearance of a person is the first thing that catches the eye of others. Therefore, being presentable at all times is of considerable importance. Here, comes the role of a Beauty Therapist, who carries out various beauty treatments on a person to improve her/his overall look, which includes dressing-up appropriately, putting the right make-up, skincare and hairstyle. Besides, s/he gives wellness treatments, including manicure and pedicure, which involve massage, followed by after care advice, to clients for relaxation. Sometimes, they are also suggested a balanced diet and nutrition, and a daily exercise regimen to maintain a healthy lifestyle.\n")
    def baw():
        print("\nThe outward appearance of a person is the first thing that catches the eye of others. Therefore, being presentable at all times is of considerable importance. Here, comes the role of a Beauty Therapist, who carries out various beauty treatments on a person to improve her/his overall look, which includes dressing-up appropriately, putting the right make-up, skincare and hairstyle. Besides, s/he gives wellness treatments, including manicure and pedicure, which involve massage, followed by after care advice, to clients for relaxation. Sometimes, they are also suggested a balanced diet and nutrition, and a daily exercise regimen to maintain a healthy lifestyle.\n")

class TravelAndTourism:
    if voc_sub_input == 406:
        print("\nIn an increasingly globalised world with the changing paradigm of urbanized living the demand for Tourism has increased manifold the world over. India has emerged as an attractive tourism destination for all types of tourists around the year resulting in Travel & Tourism taking its place among the key industries in the economy. It employs large number of work forces and its contribution to the national income is very substantial.\n")
    def tat():
        print("\nIn an increasingly globalised world with the changing paradigm of urbanized living the demand for Tourism has increased manifold the world over. India has emerged as an attractive tourism destination for all types of tourists around the year resulting in Travel & Tourism taking its place among the key industries in the economy. It employs large number of work forces and its contribution to the national income is very substantial.\n")

class HealthCare:
    if voc_sub_input == 413:
        print("\nIn an increasingly globalised world with the changing paradigm of urbanized living the demand for Tourism has increased manifold the world over. India has emerged as an attractive tourism destination for all types of tourists around the year resulting in Travel & Tourism taking its place among the key industries in the economy. It employs large number of work forces and its contribution to the national income is very substantial.\n")        
    def hc():
        print("\nIn an increasingly globalised world with the changing paradigm of urbanized living the demand for Tourism has increased manifold the world over. India has emerged as an attractive tourism destination for all types of tourists around the year resulting in Travel & Tourism taking its place among the key industries in the economy. It employs large number of work forces and its contribution to the national income is very substantial.\n")

class FinancialManagement:
    if voc_sub_input == 405:
        print("\nFinancial management refers to the management of financial funds and enterprise capital that is used to meet the overall needs and objectives of the business enterprise. The management of capital funds includes the expenditure, conservation, and investment of the enterprise’s capital.\n")        
    def fm():
        print("\nFinancial management refers to the management of financial funds and enterprise capital that is used to meet the overall needs and objectives of the business enterprise. The management of capital funds includes the expenditure, conservation, and investment of the enterprise’s capital.\n")

class main(InformationTechnology, ArtificialIntelligence, BeautyAndWellness, TravelAndTourism, HealthCare, FinancialManagement):
    def __init__(self) -> None:
        if voc_sub_input == 417:
            ArtificialIntelligence.ai()
        elif voc_sub_input == 402:
            InformationTechnology.it()
        elif voc_sub_input == 407:
            BeautyAndWellness.baw
        elif voc_sub_input == 406:
            TravelAndTourism.tat
        elif voc_sub_input == 413:
            HealthCare.hc
        elif FinancialManagement == 405:
            FinancialManagement.fm
        else:
            print("Sorry I couldn't find any results based on your input.")
object = main


#class 10

if grade_input == 10:
    print("Okay let's start")

print("\nIf you are in 10th, we will start by telling you the 'Common Mistakes Students Make While Selecting Streams'\n")

print("The most common things are -->\n\n(1) Lack of Proper Research \n(2) Ignore Their Interests and Follow Others \n(3) Peer Pressure \n(4) Follow Their Parents Dream \n(5) Family’s Socio-Economic Pressure \n(6) Aptitude Mismatch \n(7) Ignore the Need for Professional Consultation\n")

print("Now, let's tell you about 'How to Help Students on Stream Selection After 10th?'")

print("\nThe best ways to select a stream are -->\n\n(1) Career Options After 10th \n(2) Know Their Interests & Check Aptitude \n(3) Assess Their Strengths and Weaknesses \n(4) Let Them Know About Different Streams \n(5) Know About Parents Expectations \n(6) Bridge the Gap Between Parents Expectations & Child’s Abilities \n(7) Regular Follow-up with the Child \n(8) Analyze Every Aspect & Suggest A Suitable Stream\n")

print("\nThe most commonly selected streams are \n(1) Science \n(2) Commerce \n(3) Arts/Humanities\n")

stream_input = int(input("Enter the serial number present before the stream to know top carrer options in that stream: "))


class Science:
    if stream_input == 1:
        print("\n(1) Engineering \n(2) Doctor \n(3) Scientist \n(4) Astronauts \n(5) Pharmacists \n(6) Software Programmers \n(7) Web Developers")
    def sci():
        print("\n(1) Engineering \n(2) Doctor \n(3) Scientist \n(4) Astronauts \n(5) Pharmacists \n(6) Software Programmers \n(7) Web Developers")

class Commerce:
    if stream_input == 2:
        print("\n(1) Chartered Accountants (CA) \n(2) Company Secretaries (CS) \n(3) Chief Financial Accountant (CFA) \n(4) Financial Planner \n(5) Lawyer \n(6) Bank PO")
    def com():
        print("\n(1) Chartered Accountants (CA) \n(2) Company Secretaries (CS) \n(3) Chief Financial Accountant (CFA) \n(4) Financial Planner \n(5) Lawyer \n(6) Bank PO")

class ArtsHumanities:
    if stream_input == 3:
        print("\n(1) Journalism \n(2) Teaching \n(3) Lawyer \n(4) Graphic Designer \n(5) Hotel Management\n")
    def arthum():
        print("\n(1) Journalism \n(2) Teaching \n(3) Lawyer \n(4) Graphic Designer \n(5) Hotel Management\n")

class main2(ArtsHumanities, Commerce, Science):
    def __init__(self) -> None:
        if grade_input == 1:
            Science.sci
        elif grade_input == 2:
            Commerce.com
        elif grade_input == 3:
            ArtsHumanities.arthum
        else:
            print("Sorry I couldn't find any results based on your input.")

object = main2


#class 12
if grade_input == 12:
    print("Okay let's start!")
else:
    print("Bye")

print("\nIf you are in grade 12th, you might need to decide what carrer you want to persue!")

print("\nSo let's guide you about some unexplored carrer options after you are HSC/Intermediate also known as 12th Passed")

print("\nSome of the best unexplored options are given below --> \n(1) Sound Engineering \n(2) Sales \n(3) Photography \n(4) Bartending \n(5) Culinary Arts \n(6) Psycology \n(7) Cabin Crew \n(8) ")




