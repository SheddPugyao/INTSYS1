enrollment_queries = [
    # CS Courses
    "What are the subjects for Computer Science in the first semester of the first year?",
    "The subjects for Computer Science in the first semester of the first year are: INTRCS1 - Introduction to Computing Systems, PLFORM1 - Program Logic Formulation, THSELF1 - Understanding the Self, RPHIST1 - Reading in Philippine History, MATHMW1 - Mathematics in the Modern World, PRPCOM1 - Purposive Communication, NSTPRO1 - National Service Training Program 1, HCORDI1 - Cordillera: History and Socio-Cultural Heritage, SOCORN2 - Social Orientation.",
    "What are the subjects for Computer Science in the second semester of the first year?",
    "The subjects for Computer Science in the second semester of the first year are: SITNET1 - Networks and Communications, PROGIT1 - Computer Programming, HUMCOM1 - Human Computer Interaction, DITRUC1 - Discrete Structures 1, SCITES1 - Science, Technology, and Society, OPSYST1 - Operating Systems, CWORLD1 - The Contemporary World, NSTPRO2 - National Service Training Program 2, PATHFT2 - Exercise-based Fitness Activities.",
    "What are the subjects for Computer Science in the first semester of the second year?",
    "The subjects for Computer Science in the first semester of the second year are: IMDBSE1 - Information Management and Database System, PROGIT2 - Object-Oriented Programming, APPDEV1 - Introduction to Applications Development, ITMGNT - Project Management, DITRUC2 - Discrete Structures 2, DSALGO1 - Data Structures and Algorithms, GETHCS1 - Ethics, PATHFT3D - Bowling.",
    "What are the subjects for Computer Science in the second semester of the second year?",
    "The subjects for Computer Science in the second semester of the second year are: IMDBSE2 - Advanced Database Systems, ENGGSF1 - Software Engineering 1, INASSE1 - Informations Assurance and Security, WEBSYS1 - Web Systems and Technologies 1, ALGCOM1 - Algorithm and Complexity, ENGMAT9 - Probability and Statistics, GELECT2 - General Elective 2 (Gender and Society), PATFT4A - Basketball/Volleyball.",
    "What are the subjects for Computer Science in the first semester of the third year?",
    "The subjects for Computer Science in the first semester of the third year are: GAMDES1 - Introduction to Game Design and Development, WEBSYS2 - Web Systems and Technologies 2, ENGGSF2 - Software Engineering 2, INTSYS1 - Intelligent Systems, DIGDES1 - Digital Design, METHOD1 - Methods of Research, AUTHFL1 - Automata Theory and Formal Languages.",
    "What are the subjects for Computer Science in the second semester of the third year?",
    "The subjects for Computer Science in the second semester of the third year are: CMARCH1 - Computer Architecture and Organization, QASSUR1 - Quality Assurance, MOBCOM1 - Mobile Computing, PPLANG1 - Principles of Programming Languages, ENTECH1 - Technopreneurship, THESCS1 - CS Thesis Writing 1, DATSCI1 - Introduction to Data Science.",
    "What are the subjects for Computer Science in the first semester of the fourth year?",
    "The subjects for Computer Science in the first semester of the fourth year are: SOPRAC1 - Social Issues and Professional Practice, EMTECH1 - Emerging Technologies, THESCS2 - CS Thesis Writing 2, LRIZAL1 - Life and Works of Jose Rizal, GELECT3 - General Elective 3 (People and the Earth's Ecosystem), ARTAPP1 - Art Appreciation.",
    "What are the subjects for Computer Science in the second semester of the fourth year?",
    "The subjects for Computer Science in the second semester of the fourth year are: BCSOJT1 - Practicum (490 hours)."

    # COE Courses
    "What are the subjects for Computer Engineering in the first semester of the first year?",
    "The subjects for Computer Engineering in the first semester of the first year are: CHMENG1 - Chemistry for Engineers, DIFCAL1 - Calculus 1, CPEPRO1 - Programming Logic and Design, COMDIS1 - Computer Engineering as a Discipline, THSELF1 - Understanding the World, PRPCOM1 - Purposive Communication, MATHMW1 - Mathematics in the Modern World, NSTPRO1 - National Service Training Program 1, HCRODI1 - Cordillera: History and Socio-Cultural Heritage, PATHFT1 - Movement Competency Training, SOCORN2 - Social Orientation.",
    "What are the subjects for Computer Engineering in the second semester of the first year?",
    "The subjects for Computer Engineering in the second semester of the first year are: INTCAL1 - Calculus 2, CPEPHS1 - Physics for Engineering, DISMAT1 - Discrete Mathematics, CPEPRO2 - Object-oriented Programming, CPENET1 - Intro. to Networks and Data Communication, SCITES1 - Science, Technology, Engg and Society, NSTPRO2 - National Service Training Program 2, PATHFT2 - Exercise-based Fitness Activities.",
    "What are the subjects for Computer Engineering in the first semester of the second year?",
    "The subjects for Computer Engineering in the first semester of the second year are: ENVCPE1 - Environmental Science and Engineering, ENGMAT7 - Differential Equations, CIRCPE1 - Fundamentals of Electrical Circuits, DATALG1 - Data Structures and Algorithms, SITNET2 - Routing and Switching Technologies, CADCPE1 - Computer-Aided Drafting, ENGECO1 - Engineering Economy, LRIZAL1 - Life and Works of Rizal, CWORLD1 - The Contemporary World, PATHFT3D - Bowling.",
    "What are the subjects for Computer Engineering in the second semester of the second year?",
    "The subjects for Computer Engineering in the second semester of the second year are: CPENUM1 - Numerical Methods, ELECPE1 - Fundamentals of Electronic Circuits, IMDBSE1 - Information Management and Database Systems, CPEOPR1 - Operating Systems, SITNET3 - Scaling Networks, GETHICS1 - Ethics, ARTAPP1 - Art Apppreciation, PATHFT4A - Basketball/Volleyball.",
    "What are the subjects for Computer Engineering in the first semester of the third year?",
    "The subjects for Computer Engineering in the first semester of the third year are: CNTCPE1 - Feedback and Control System, LOGCPE1 - Logic Circuit and Design, COMCPE1 - Data and Digital Communications, MIXCPE1 - Fundamentals of Mixed Signals and Sensors, CADCPE2 - Computer Engineering Drafting and Design, MICCPE1 - Microelectronics 1, HDLCPE1 - Intro. To Hardware Description Language, CPESOF1 - Software Design, RPHIST1 - Readings in Philippine History.",
    "What are the subjects for Computer Engineering in the second semester of the third year?",
    "The subjects for Computer Engineering in the second semester of the third year are: CPESAF1 - Basic Occupational Health and Safety, DIGISP1 - Digital Signal Processing, MROCPE1 - Microprocessors, MICCPE2 - Microelectronics 2, CPEMET1 - Methods of Research, ENTECH1 - Technopreneurship, CPELAW1 - CPE Laws and Professional Practice, GELECT2 - General Elective 2 (Gender and Society).",
    "What are the subjects for Computer Engineering in the first semester of the fourth year?",
    "The subjects for Computer Engineering in the first semester of the fourth year are: CPEMRG1 - Emerging Technologies in CpE, GELECT3 - General Elective 3 (People and Earth's Ecosystem), PROCPE1 - CpE Practice and Design 1, EMBCPE1 - Embedded Systems, COWASM1 - Computer Architecture and Organization, MICCPE3 - Microelectronics 3, CPEMGT1 - Engineering Management, PLDTRP1 - Seminars and Fieldtrips.",
    "What are the subjects for Computer Engineering in the second semester of the fourth year?",
    "The subjects for Computer Engineering in the second semester of the fourth year are: PROCPE2 - CpE Practice and Design 2, OJTCPE1 - Practicum (369 hrs)."

    # IT Courses
     "What are the subjects for Information Technology in the first semester of the first year?",
    "The subjects for Information Technology in the first semester of the first year are: INTRCS1 - Introduction to Computing Systems, PLFORM1 - Program Logic Formulation, THSELF1 - Understanding the Self, RPHIST1 - Reading in Philippine History, MATHMW1 - Mathematics in the Modern World, PRPCOM1 - Purposive Communication, NSTPRO1 - National Service Training Program 1, PATHFT1 - Movement Competency Training or MCT, HCORDI1 - Cordillera: History and Socio-Cultural Heritage, SOCORN2 - Social Orientation.",
    "What are the subjects for Information Technology in the second semester of the first year?",
    "The subjects for Information Technology in the second semester of the first year are: SITNET1 - Networks and Communications, PROGIT1 - Computer Programming, HUMCOM1 - Human Computer Interaction, DITRUC1 - Discrete Structures 1, SCITES1 - Science, Technology, and Society, CWORLD1 - The Contemporary World, NSTPRO2 - National Service Training Program, PATHFT2 - Exercise-based Fitness Activities.",
    "What are the subjects for Information Technology in the first semester of the second year?",
    "The subjects for Information Technology in the first semester of the second year are: SITNET2 - Routing and Switching Technologies, OPSYST1 - Operating System, PROGIT2 - Object-oriented Programming, ENGMAT9 - Probability and Statistics, DSALGO1 - Data Structures and Algorithm Analysis, GETHCS1 - Ethics, PATFT3D - Bowling.",
    "What are the subjects for Information Technology in the second semester of the second year?",
    "The subjects for Information Technology in the second semester of the second year are: SITNET3 - Scaling Networks, IMDBSE1 - Information Management and Database Systems, SERADM1 - Server Administrator, APPDEV1 - Introduction to Application Development, SYSINT1 - System Integration and Agriculture 1, GELECT2 - General Elective 2 (Gender Society), WNCOMP1 - Wireless and Mobile Computing, PATFT4A - Basketball/Volleyball.",
    "What are the subjects for Information Technology in the first semester of the third year?",
    "The subjects for Information Technology in the first semester of the third year are: CERTIF1 - Certification Exam, WEBSYS1 - Web System and Technologies 1, IMDBSE2 - Advanced Database System, NETANA1 - Network Analysis and Design, SYSADM1 - System Administration and Maintenance, SYSINT2 - System Integration and Architecture 2, INASEC1 - Information Assurance and Security 1, ENTECH1 - Technopreneurship, METHOD1 - Methods of Research.",
    "What are the subjects for Information Technology in the second semester of the third year?",
    "The subjects for Information Technology in the second semester of the third year are: CMARCH1 - Computer Architecture and Organization, ITMGNT1 - Project Management, INASEC2 - Information Assurance and Security 2, THESIT1 - Capstone Project and Research 1, NETPRO1 - Network Programming, LRIZAL1 - Life and Works of Jose Rizal.",
    "What are the subjects for Information Technology in the first semester of the fourth year?",
    "The subjects for Information Technology in the first semester of the fourth year are: SOPRAC1 - Social Issues and Professional Practice, EMTECH1 - Emerging Technologies, THESIT2 - Capstone Project and Research 2, GELECT3 - General Elective 3 (People and the Earth's Ecosystem), ARTAPP1 - Art Appreciation.",
    "What are the subjects for Information Technology in the second semester of the fourth year?",
    "The subjects for Information Technology in the second semester of the fourth year are: BITOJT1 - Practicum(490 hours)."

    # ACT-MWD Courses
    "What are the subjects for Multimedia and Web Design in the first semester of the first year?",
    "The subjects for Multimedia and Web Design in the first semester of the first year are: INTRCS1 - Introduction to Computing Systems, PROPHY1 - Computer Programming 1, ARTAPP1 - Art Appreciation, MATHMW1 - Mathematics in the Modern World, ACTDRW1 - Freehand and Digital Drawing, NSTPRO1 - National Service Training Program 1, HCORDI1 - Cordillera: History and Socio-Cultural Heritage, PATHFT1 - Movement Competency Training, SOCORN2 - Social Orientation.",
    "What are the subjects for Multimedia and Web Design in the second semester of the first year?",
    "The subjects for Multimedia and Web Design in the second semester of the first year are: PROPHY2 - Object-Oriented Programming with Flask, ACTSOP1 - Professional Issues in Computing, ACTGRH1 - Graphics Design, ACTHUM1 - Web Design, CWORLD1 - The Contemporary World, NSTPRO2 - National Service Training Program 2, PATHFT2 - Exercise-based Fitness Activities.",
    # ACT Courses
    "What are the subjects for Associate in Computer Technology in the first semester of the first year?",
    "The subjects for Associate in Computer Technology in the first semester of the first year are: INTRCS1 - Introduction to Computing Systems, PLFORM1 - Program Logic Formulation, THSELF1 - Understanding the Self, ARTAPP1 - Art Appreciation, MATHMW1 - Mathematics in the Modern World, PRPCOM1 - Purposive Communication, NSTPRO1 - National Service Training Program 1, EDPHYS1 - PE Elective 1, SOCORN1 - Social Orientation.",
    "What are the subjects for Associate in Computer Technology in the second semester of the first year?",
    "The subjects for Associate in Computer Technology in the second semester of the first year are: SITNET1 - Networks and Communications, PROGIT1 - Computer Programming, HUMCOM1 - Human Computer Interaction, DITRUC1 - Discrete Structures 1, DIGIMD1 - Digital Media 1, CWORLD1 - The Contemporary World, NSTPRO2 - National Service Training Program 2, EDPHYS2 - PE Elective 2."
]

process_one = [
    "Hi, I'm a new student. How do I enroll for courses?",
    "Welcome! Here are the steps for enrollment. newline1. Check the schedule of enrollment posted on the UB Website and official Facebook page. newline2. Log in to the UB student portal with your username, birthdate, and password. newline3. Register your preferred course/s and schedule. newline4. Contact the Enrollment Adviser/Secretary/Dean of the school regarding concerns about the subjects or the enrollment system through official email or Facebook account of the school. newline5. Pay the required down payment in any of the accredited banks or at the UB Cashier. newline6. View your schedule on the Student Portal. newline7. Proceed to the MIS Office at F building for your school ID validation."
]

process_two = [
    "What are the admission requirements for incoming freshmen?",
    "For incoming freshmen, the admission requirements include: newlineCertified true copy of Grade 11 report card (F-138/SF9) with complete and passing grades and Grade 12 First Semester Report Card (F-138/SF9) duly signed by the school principal; or newlineCertificate of No Failing Grades filled out by the school principal.newlinePhotocopy of PSA Birth Certificate. newlineFor more details, you can visit the enrollment page on the UB website."
]

process_three = [
    "Can you tell me about the reservation procedures for incoming freshmen?",
    "Certainly! Here are the online reservation procedures for incoming freshmen: newline1. Register at UB Student Portal. newline2. Click Apply as a New Student and complete all the needed information. newline3. Download and fill-out the Declaration and Waiver Form and Data Privacy Consent Form. newline4. Pay the Admission Processing Fee of Php 1,000.00 to any UB accredited Banks. newline5. Prepare and scan the admission requirements (PDF format ONLY) and upload them. newline 6. Go to the New Student Online Credentials Submission Form and upload the scanned copy of admission requirements and reservation fee acknowledgment receipt. newline7. Once the needed admission documents are verified and accepted, ARC staff will approve the application for reservation. newline8. Courses will be reserved based on the student's program and curriculum. newline9. You shall receive a confirmation email of your reservation with your UB student ID number."

]

question = [
    "What's the deadline for enrollment?",
    "The deadline for enrollment for incoming freshmen/transferees for the First Semester of Academic Year 2024-2025 is until August 12, 2024. It's important to complete your enrollment process before this date to secure your slot."
]

programs = [
    "Hi, I'm interested in enrolling for a program. What options do you have?",
    "We offer the following programs: newlineBSCS - Bachelor of Science in Computer Science newlineBSCOE - Bachelor of Science in Computer Engineering newlineBSIT - Bachelor of Science in Information Technology newlineACT - Associate in Computer Technology newlineACT-MWD - Associate in Computer Technology with Specialization in Multimedia",

]