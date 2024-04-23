import socket
from threading import Thread
import random

AF_INET = socket.AF_INET
SOCK_STREAM = socket.SOCK_STREAM

# Create a TCP/IP socket
sock = socket.socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
ip_address = '127.0.0.1'
port = 8000

sock.bind((ip_address, port))
sock.listen()

# Create a list of clients
clients = []

# Create a list of nicknames
nicknames = []

# Print that the server is running
print("Server is running...")

# Define question and answer (MCQs)
questions = [
    "What is the capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Kolkata\n(d) Chennai\n",
    "What is the capital of Australia?\n(a) Sydney\n(b) Melbourne\n(c) Canberra\n(d) Perth\n",
    "What is the capital of Canada?\n(a) Vancouver\n(b) Toronto\n(c) Ottawa\n(d) Montreal\n",
    "What is the capital of France?\n(a) Paris\n(b) Marseille\n(c) Lyon\n(d) Toulouse\n",
    "What is the capital of Germany?\n(a) Berlin\n(b) Hamburg\n(c) Munich\n(d) Cologne\n",
    "What is the capital of Italy?\n(a) Rome\n(b) Milan\n(c) Naples\n(d) Turin\n",
    "What is the capital of Japan?\n(a) Tokyo\n(b) Osaka\n(c) Kyoto\n(d) Yokohama\n",
    "What is the capital of Russia?\n(a) Moscow\n(b) Saint Petersburg\n(c) Novosibirsk\n(d) Yekaterinburg\n",
    "What is the capital of South Korea?\n(a) Seoul\n(b) Busan\n(c) Incheon\n(d) Daegu\n",
    "What is the capital of Spain?\n(a) Madrid\n(b) Barcelona\n(c) Valencia\n(d) Seville\n",
    "What is the capital of United Kingdom?\n(a) London\n(b) Birmingham\n(c) Glasgow\n(d) Liverpool\n",
    "What is the capital of United States?\n(a) Washington, D.C.\n(b) New York City\n(c) Los Angeles\n(d) Chicago\n",
    "What is the capital of Brazil?\n(a) Brasilia\n(b) Rio de Janeiro\n(c) Sao Paulo\n(d) Salvador\n",
    "What is the capital of Argentina?\n(a) Buenos Aires\n(b) Cordoba\n(c) Rosario\n(d) Mendoza\n",
    "What is the capital of Chile?\n(a) Santiago\n(b) Valparaiso\n(c) Concepcion\n(d) La Serena\n",
    "What is the capital of Colombia?\n(a) Bogota\n(b) Medellin\n(c) Cali\n(d) Barranquilla\n",
    "What is the capital of Peru?\n(a) Lima\n(b) Arequipa\n(c) Trujillo\n(d) Chiclayo\n",
    "What is the capital of Venezuela?\n(a) Caracas\n(b) Maracaibo\n(c) Valencia\n(d) Barquisimeto\n",
    "What is the capital of Egypt?\n(a) Cairo\n(b) Alexandria\n(c) Giza\n(d) Shubra El-Kheima\n",
    "What is the capital of South Africa?\n(a) Cape Town\n(b) Johannesburg\n(c) Durban\n(d) Pretoria\n",
    "What is the capital of Nigeria?\n(a) Lagos\n(b) Kano\n(c) Ibadan\n(d) Abuja\n",
    "What is the capital of Kenya?\n(a) Nairobi\n(b) Mombasa\n(c) Nakuru\n(d) Eldoret\n",
    "What is the capital of Morocco?\n(a) Rabat\n(b) Casablanca\n(c) Fez\n(d) Tangier\n",
    "What is the capital of Algeria?\n(a) Algiers\n(b) Oran\n(c) Constantine\n(d) Annaba\n",
    "What is the capital of Tunisia?\n(a) Tunis\n(b) Sfax\n(c) Sousse\n(d) Kairouan\n",
    "What is the capital of Saudi Arabia?\n(a) Riyadh\n(b) Jeddah\n(c) Mecca\n(d) Medina\n",
    "What is the capital of Turkey?\n(a) Ankara\n(b) Istanbul\n(c) Izmir\n(d) Bursa\n",
    "What is the capital of Iran?\n(a) Tehran\n(b) Mashhad\n(c) Isfahan\n(d) Karaj\n",
    "What is the capital of Iraq?\n(a) Baghdad\n(b) Basra\n(c) Mosul\n(d) Erbil\n",
    "What is the capital of Pakistan?\n(a) Islamabad\n(b) Karachi\n(c) Lahore\n(d) Faisalabad\n",
    "What is the capital of China?\n(a) Beijing\n(b) Shanghai\n(c) Guangzhou\n(d) Shenzhen\n",
    "What is the capital of Thailand?\n(a) Bangkok\n(b) Nonthaburi\n(c) Nakhon Ratchasima\n(d) Chiang Mai\n",
    "What is the capital of Vietnam?\n(a) Hanoi\n(b) Ho Chi Minh City\n(c) Haiphong\n(d) Da Nang\n",
    "What is the capital of Indonesia?\n(a) Jakarta\n(b) Surabaya\n(c) Bandung\n(d) Bekasi\n",
    "What is the capital of Malaysia?\n(a) Kuala Lumpur\n(b) Johor Bahru\n(c) Ipoh\n(d) Kuching\n",
    "What is the capital of Singapore?\n(a) Singapore\n(b) Woodlands\n(c) Jurong East\n(d) Tampines\n",
    "What is the capital of Philippines?\n(a) Manila\n(b) Quezon City\n(c) Davao City\n(d) Caloocan\n"
]

answers = ['a', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'a', 'a', 'a', 'a']

def get_random_question_answer(conn):
    # Check whether there are any questions left
    if len(questions) == 0:
        conn.send("No questions left!".encode('utf-8'))
        return None, None, None
    else:
        # Get a random question and answer
        random_index = random.randint(0, len(questions) - 1)
        question = questions[random_index]
        answer = answers[random_index]
        conn.send(question.encode('utf-8'))
        return random_index, question, answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def remove(client):
    # Remove client from list of clients
    if client in clients:
        clients.remove(client)

def remove_nickname(nickname):
    # Remove nickname from list of nicknames
    if nickname in nicknames:
        nicknames.remove(nickname)

def clientthread(conn,nickname):
    score = 0
    conn.send("Welcome to the quiz!".encode('utf-8'))
    conn.send(f"You will be asked {len(answers)} questions. Each question is worth 1 point.".encode('utf-8'))
    conn.send("Good luck!\n\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)

    while True:
        try:
            msg = conn.recv(2048).decode('utf-8')
            if msg:
                if msg.lower() == answer:
                    score += 1
                    conn.send(f"Correct! Your score is {score}\n".encode('utf-8'))
                else:
                    conn.send("Incorrect!\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
                if question is None:
                    conn.send(f" Your final score is {score}\n".encode('utf-8'))
                    break
                print(answer)
            else:
                remove(conn)
                remove_nickname(nickname)
        except Exception as e:
            print(str(e))
            continue

while True:
    conn, addr = sock.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    clients.append(conn)
    nicknames.append(nickname)
    print(nickname + " connected")
    thread = Thread(target = clientthread, args = (conn,nickname))
    thread.start()