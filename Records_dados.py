from pyrecord import Record

dadosHome = Record.create_type('time','qtdeJogos','Vitórias','Derrotas','Empates','MediaGolsMarcados','JogosSemMarcar','MediaGolsSofridos','JogosSemSofrer','MarcouOver0_5','MarcouOver1_5','MarcouOver2_5','Sofreu0_5','Sofreu1_5','Sofreu2_5','Escanteios','ChutesNoGol','ChutesPraFora','Finalizacoes','Impedimentos','Laterais','TiroDeMeta','Faltas','CartoesAmarelos','CartoesVermelhos')

dadosVisitante = Record.create_type('time','qtdeJogos','Vitórias','Derrotas','Empates','MediaGolsMarcados','JogosSemMarcar','MediaGolsSofridos','JogosSemSofrer','MarcouOver0_5','MarcouOver1_5','MarcouOver2_5','Sofreu0_5','Sofreu1_5','Sofreu2_5','Escanteios','ChutesNoGol','ChutesPraFora','Finalizacoes','Impedimentos','Laterais','TiroDeMeta','Faltas','CartoesAmarelos','CartoesVermelhos')



''' EXEMPLOS DE USO DE RECORDS EM PYTHON
Person = Record.create_type("Person", "name", "email_address")
Student = Person.extend_type("Student", "courses_read", "graduation_date", graduation_date=None)
Professor = Person.extend_type("Professor", "course_taught")

john_student = Student("John Smith", "jsmith@example.org", ["Calculus", "Economics"])
john_professor = Professor("John Doe", "john.doe@example.com", "OOP")
john_professor2 = Professor(email_address="john.doe@example.com", name="John Doe", course_taught="OOP")
jane_student = Student("Jane Doe", "jane.doe@example.org", ["Calculus", "OOP"], datetime(1995, 10, 4))
jane_professor = Professor("Jane Doe", "jane.doe@example.org", "Calculus")
alice_student = Student("Alice Smith", "alice.smith@example.org")

fonte: https://pythonhosted.org/pyrecord/

'''