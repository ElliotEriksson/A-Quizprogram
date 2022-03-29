from resources import Questions

question_bank = []

options1 = ["(1) Coax", "(2) Ethernet", "(3) Fiber", "(4) TP"]
options2 = ["(1) 150m", "(2) 100m", "(3) 50m", "(4) 200m"]
options3 = ["(1) Domain Number System", "(2) Domain Name Supplier", "(3) Domain Name System", "(4) Domain Number Supplier"]
options4 = ["(1) Domain Host Control Protocol", "(2) Domain Host Configuration Partition", "(3) Domain Host Configuration Protocol", "(4) Domain Head Control Partition"]
options5 = ["(1) Cat 3", "(2) Cat 5", "(3) Cat 5e", "(4) Cat 6"]
options6 = ["(1) Gigabyte Interface Control", "(2) Gigabit Internship Controller", "(3) Gigabit Interface Converter",  "(4) Gigabit Interface Control"]
options7 = ["(1) UTP", "(2) ScTP", "(3) STP", "(4) FTP"]

question1 = Questions("Vilken kabel används i tvnät?", options1, "(1) Coax")
question2 = Questions("Hur lång kan en ethernet kabel vara?", options2, "(2) 100m")
question3 = Questions("Vad står DNS för?", options3, "(3) Domain name system")
question4 = Questions("Vad står DHCP för?", options4, "(3) Domain Host Configuration Protocol")
question5 = Questions("Vilken är den bästa ethernet kabeln?", options5, "(4) Cat 6")
question6 = Questions("Vad står GBIC för?", options6, "(3) Gigabit Interface Converter")
question7 = Questions("Vilken är den vanligaste typen av ethernet kabel?", options7, "(1) UTP")

question_bank.append(question1.save_question())
question_bank.append(question2.save_question())
question_bank.append(question3.save_question())
question_bank.append(question4.save_question())
question_bank.append(question5.save_question())
question_bank.append(question6.save_question())
question_bank.append(question7.save_question())

with open('questions.txt', 'w', encoding="utf-8") as f:
    for list in question_bank:
        f.write('%s\n' % list)