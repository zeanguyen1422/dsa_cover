

# pointer object recursion + call stack 

# bro brain faure, bro swe, bro noob coder

"""
In computer science, a pointer is an object in many programming languages that stores a memory address

A pointer references a location in memory

Using pointers significantly improves performance for repetitive operations, like traversing iterable data structures 
(e.g. strings, lookup tables, control tables and tree structures)


# allocate memory 

# Dynamic memory allocation is the process of assigning the memory space during the execution time or the run time of code 

When we do not know how much amount of memory would be needed for the program beforehand.
When we want data structures without any upper limit of memory space.
When you want to use your memory space more efficiently.Example: If you have allocated memory space for a 1D array 
as array[20] and you end up using only 10 memory spaces then the remaining 10 memory spaces would be wasted and this wasted memory 
cannot even be utilized by other program variables.
Dynamically created lists insertions and deletions can be done very easily just by the manipulation of addresses whereas in case of 
statically allocated memory insertions and deletions lead to more movements and wastage of memory.
When you want you to use the concept of structures and linked list in programming, dynamic memory allocation is a must 

dwqoijdoiqj



A thread refers to an execution unit in the process that has its own programme counter, 
stack, as well as a set of registers. Threads aren’t actually allowed to exist outside a proces 


# https://www.lenovo.com/us/en/glossary/dereference-operator/?orgRef=https%253A%252F%252Fwww.google.com%252F
# https://byjus.com/gate/what-is-thread-in-operating-system-notes/#:~:text=A%20thread%20refers%20to%20a,process%20can%20have%20several%20threads.
# https://www.geeksforgeeks.org/what-is-dynamic-memory-allocation/


"""


"""
Variant In A Simple Program Statement 


# internal external memory, main memory secondary memory auxiliary memory 

# lý thuyết nặng quá 

# cpu 
# register (memory address instruction opcode) và các lệnh) <-- register dùng cho cache 
# ram hdd 
# input output show ra á 
# file management và các format định dang file của nó để người ta quản lý á 
# rác rưởi wikipedia 
# rác rưởi twitter 
# instruction bao gồm opcode và memory address hex
# load add đồ á, opcode 4 bit với memory address nhân với nhau là ra instruction, instruction để cpu xử lý 
# load add là binary 4 interger, còn memory address là 0x001 0x002 kiểu v 
# input output store add instructions 
# address, instruction, comment 
"""
"""
One key difference between most assembly languages and high–level languages that are
compiled is that the latter do not require explicit declaration of memory locations, as was done above. 
A compiler just requires a type definition, from which it will automatically generate the storage assignments
"""



# http://www.edwardbosworth.com/CPSC2105/Lectures/Slides_05/Chapter_04/MARIE_AssemblyLanguage.htm --> đọc rồi, hay á 


"""
https://www.techtarget.com/whatis/definition/POP3-Post-Office-Protocol-3
https://developers.google.com/gmail/imap/imap-smtp#:~:text=For%20non%2DGmail%20clients%2C%20Gmail,industry%2Dstandard%20OAuth%202.0%20protocol.
https://vi.wikipedia.org/wiki/Internet_Message_Access_Protocol
https://support.microsoft.com/vi-vn/office/imap-v%C3%A0-pop-l%C3%A0-g%C3%AC-ca2c5799-49f9-4079-aefe-ddca85d5b1c9
https://www.linkedin.com/pulse/overview-bluetooth-ble-protocols-osi-layers-rasmita-nayak#:~:text=The%20commonly%20adopted%20protocols%20used,Wireless%20Application%20Protocol%20(WAP).


"""
"""
https://ardc.edu.au/resource/standardised-communications-protocols/#:~:text=A%20communications%20protocol%20is%20a,Hypertext%20Transfer%20Protocol%20(HTTP)
https://www.techtarget.com/searchnetworking/definition/fiber-optics-optical-fiber
https://study.com/learn/lesson/pseudocode-examples-how-to.html
https://stackoverflow.com/questions/70683743/how-are-code-segments-and-data-segments-of-a-source-code-program-really-handled
https://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap
https://www.techtarget.com/whatis/definition/Direct-Memory-Access-DMA
https://byjus.com/gate/what-is-thread-in-operating-system-notes/#:~:text=Benefits%20of%20Threads-,What%20is%20Thread%20in%20Operating%20Systems%3F,process%20can%20have%20several%20threads.
https://www.tutorialspoint.com/operating_system/os_multi_threading.htm#:~:text=A%20thread%20is%20a%20flow,which%20contains%20the%20execution%20history.
https://www.geeksforgeeks.org/what-is-dynamic-memory-allocation/
"""


"""

Standardised Communications Protocols
All information and communications technology relies on standardised communications protocols to operate effectively. 

A communications protocol is a set of formal rules describing how to transmit or exchange data, especially across a network. 
A standardised communications protocol is one that has been codified as a standard. Examples of these include WiFi, the Internet Protocol, 
and the Hypertext Transfer Protocol (HTTP).

The FAIR data principles state that data and metadata should be made accessible with standardised communications protocols 
on the internet and in applications.  

Read more about the FAIR data principles.

Layer Models
Modern communications protocols rarely operate in isolation and depend on other protocols in a layered model known as a stack. 
Each layer in a stack relies on those below it, and provides for the layers above. For example, the internet works using the TCP/IP stack, 
which is divided into four layers 

ethernet protocol ip tcp udp http pop3


The public service by which letters and parcels are collected and delivered is usually called the post in British English and the mail in American English.

post mail người ta gửi truyền thống á 

a room or part of a building in which people work, especially sitting at tables with computers, phones, etc., usually as a part of a business or other organization:
the director's office
I didn't leave the office until eight o'clock last night.
office equipment
office workers



còn post office là bưu điện 


protocol là nghi thức, giao thức 

a computer language allowing computers that are connected to each other to communicate

POP3 là giao thức máy khách-máy chủ một chiều trong đó email được nhận và lưu giữ trên máy chủ email. "3" đề cập đến phiên bản thứ ba của giao thức POP gốc.

Người nhận hoặc ứng dụng email của họ có thể tải xuống thư định kỳ từ máy chủ bằng POP3. Do đó, POP3 cung cấp phương tiện tải email từ máy chủ về máy khách để người nhận có thể xem email ngoại tuyến. POP3 có thể được coi là dịch vụ "lưu trữ và chuyển tiếp".

Sau khi email có trên máy khách, POP3 sẽ xóa nó khỏi máy chủ. Với một số triển khai, người dùng hoặc quản trị viên có thể chỉ định thư đó sẽ được lưu trong một thời gian, cho phép người dùng tải email xuống bao nhiêu lần tùy thích trong khoảng thời gian được chỉ định



"""




"""
djwqoidjwqoijdowiqjdowiqjowdi


post office là bưu điện 

protocal là nghi thức, giao thức 


Post Office Protocol 3, or POP3, is the most commonly used protocol for receiving email over the internet. This standard protocol, which most email servers and their clients support, is used to receive emails from a remote server and send to a local client.

POP3 is a one-way client-server protocol in which email is received and held on the email server. The "3" refers to the third version of the original POP protocol.

A recipient or their email client can download mail periodically from the server using POP3. Thus, POP3 offers a means of downloading email from a server to the client so the recipient can view the email offline. POP3 can be thought of as a "store-and-forward" service.

Once the email is on the client, POP3 then deletes it from the server. With some implementations, users or an administrator can specify that mail be saved for some time, allowing users to download email as many times as they wish within the specified period


In networking, a protocol is a set of rules for formatting and processing data. Network protocols are like a common language for computers. 
The computers within a network may use vastly different software and hardware; however, the use of protocols enables them to communicate with each other 
regardless 


decode mean


convert (a coded message) into intelligible language.
"he put down the phone and decoded the message"


chuyển đổi (một tin nhắn được mã hóa) thành ngôn ngữ dễ hiểu.
"Anh ấy đặt điện thoại xuống và giải mã tin nhắn"


to discover the meaning of information given in a secret or complicated way:
Decoding the paintings is not difficult once you know what the component parts symbolize.

dwq


encode là mã hóa, trai ngược lại với decode 


decode is the process of converting encoded or compressed data back into its original format, for example, 
when data is transmitted or stored in a compressed or encoded form, it needs to be decoded in order to be used or displayed 

mã hóa tin nhắn của 2 bên á hả à à encode message ko cho bên thứ 3 nào xem trộm tin nhắn của ngkhac 


we need to process data, transform data, interpret data in order to extract its meaning and value 



interpret ~ giải thích, diễn giải, biên dịch 

A compiler translates the entire source code into machine code before execution, 
resulting in faster execution since no translation is needed during runtime. On the other hand, an interpreter translates code line by 
line during execution, making it easier to detect errors but potentially slowing down the program  

What Does Interpreter Mean?
An interpreter is a computer program that is used to directly execute program instructions written using one of the many high-level programming languages



a definite or clear expression of something in speech or writing.
"do you agree with this statement?"


một biểu hiện rõ ràng hoặc rõ ràng của một cái gì đó trong lời nói hoặc văn bản.
"Bạn có đồng ý với tường trình này không?"


statement ~ tuyên bố, khai báo
 
a formal account of events given by a witness, defendant, or other party to the police or in a court of law.
"she made a statement to the police" 


staments ~ các báo cáo, các bản sao kê, các bản kê khai 

something you say or write that expresses an opinion
commentThe MP could not be reached for comment.
remarkHis controversial remarks about race were widely reported.
statementIn a statement released earlier today, the team denied allegations of cheating.
declarationThe sovereign made a formal declaration of war.
observationShe makes some interesting observations about human nature in her book.
commentaryI love that sports announcer's commentary - it's always so funny! 



a record of the amounts of money paid into and taken out of your bank account during a particular period of time:
Check you statement and see if the money has been taken from your bank account.
He keeps all his bank statements and files them away.


bản ghi số tiền được trả vào và rút ra khỏi tài khoản ngân hàng của bạn trong một khoảng thời gian cụ thể :
Kiểm tra bảng sao kê của bạn và xem tiền đã được lấy từ tài khoản ngân hàng của bạn chưa .
Anh ta giữ tất cả các báo cáo ngân hàng của mình và cất chúng đi.


tính từ

có tầm quan trọng sống còn; chủ yếu.
"hành động ngay lập tức là bắt buộc"



đưa ra mệnh lệnh có thẩm quyền; độc đoán.
"Chuông lại vang lên, lời kêu gọi mệnh lệnh cuối cùng"

danh từ
1 .
một điều cần thiết hoặc khẩn cấp.
"sự di chuyển lao động tự do là một mệnh lệnh kinh tế"


adj 
of vital importance; crucial.
"immediate action was imperative"

giving an authoritative command; peremptory.
"the bell pealed again, a final imperative call"


noun
1.
an essential or urgent thing.
"free movement of labor was an economic imperative"





In computer programming, a statement is a syntactic unit of an imperative programming language that expresses some action to be carried out. 
A program written in such a language is formed by a sequence of one or more statements. A statement may have internal components (e.g. expressions) 

rác rưởi wikipedia và thằng con cặc nào viết ra được mấy cái dòng này  


In a computer programming language, a statement is a line of code commanding a task. Every program consists of a sequence of statements



còn statement trong ngành gọi là câu lệnh 


syntax 

the arrangement of words and phrases to create well-formed sentences in a language.
"the syntax of English"
a set of rules for or an analysis of the syntax of a language.
plural noun: syntaxes
"generative syntax"
the branch of linguistics that deals with syntax.

sự sắp xếp các từ và cụm từ để tạo thành các câu đúng ngữ pháp trong một ngôn ngữ.
"cú pháp tiếng Anh"
một bộ quy tắc hoặc phân tích cú pháp của một ngôn ngữ
danh từ số nhiều : cú pháp
"cú pháp sáng tạo"
nhánh ngôn ngữ học liên quan đến cú pháp.

the grammatical arrangement of words in a sentence:
The examples should always illustrate correct syntax.

Sự sắp xếp ngữ pháp của các từ trong câu 
Các ví dụ phải luôn minh họa đúng cú pháp. 


Readers use their syntactic and semantic knowledge to decode the text.

Người đọc sử dụng kiến ​​thức cú pháp và ngữ nghĩa của mình để giải mã văn bản 

kiến thức cú pháp và ngữ nghĩa của mình để giải mã văn bản 


hửm ?


The 0x prefix is used in hexadecimal notation to indicate that the following characters represent a hexadecimal value. 
This prefix is used in Solidity (as well as in other programming languages and contexts) to distinguish hexadecimal values from other types of values 

semantic là ngữ nghĩa, meaning of words 

Sự sắp xếp ngữ pháp của các từ trong câu :
Các ví dụ phải luôn minh họa đúng cú pháp.


the grammatical arrangement of words in a sentence:
The examples should always illustrate correct syntax.



parse là phân tích cú pháp à 





what does 0x mean computer 

hexadecimal
The prefix 0x is used in code to indicate that the number is being written in hex. But what is 'B' doing in there? 
The hexadecimal format has a base of 16, which means that each digit can represent up to 16 different values







the process of converting something from one thing to another:
conversion of something into something Solar power is the conversion of the sun's energy into heat and electricity.


quá trình chuyển đổi một cái gì đó từ thứ này sang thứ khác:
chuyển đổi thứ gì đó thành thứ gì đó Năng lượng mặt trời là sự chuyển đổi năng lượng của mặt trời thành nhiệt và điện 


"""






































