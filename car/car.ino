#define L 0
#define R 1

#define F 0
#define B 1

#define N 2

int steerA = 8;
int steerB = 9;
int steerSpeed = 10;

int driveA = 13;
int driveB = 12;
int driveSpeed = 11;

int drive2A = 6;
int drive2B = 7;

int feedbackPin = 0;
int feedback = 0;

int steerState = 320;
int driveState = N;

byte data = 0;

void setup() {
  Serial.begin(9600);
  
  pinMode(steerA, OUTPUT);
  pinMode(steerB, OUTPUT);
  pinMode(steerSpeed, OUTPUT);

  pinMode(driveA, OUTPUT);
  pinMode(driveB, OUTPUT);
  pinMode(driveSpeed, OUTPUT);

  pinMode(drive2A, OUTPUT);
  pinMode(drive2B, OUTPUT);
}

void loop() {
  if(data == 'f') {
    driveState = F;
    steerState = 320;
  }
  else if(data == 'a') {
    driveState = F;
    steerState = 550;
  }
  else if(data == 'b') {
    driveState = F;
    steerState = 90;
  }
  else if(data == 'z') {
    driveState = B;
    steerState = 320;
  }
  else if(data == 'c') {
    driveState = B;
    steerState = 550;
  }
  else if(data == 'd') {
    driveState = B;
    steerState = 90;
  }
  else if(data == 'l') {
    driveState = N;
    steerState = 550;
  }
  else if(data == 'r') {
    driveState = N;
    steerState = 90;
  }
  else if(data == 'n') {
    driveState = N;
    steerState = 320;
  }
  
  feedback = analogRead(feedbackPin);

  if(feedback - steerState > 80) {
    steer(R, 128);
  }
  else if(feedback - steerState < -80) {
    steer(L, 128);
  }
  else {
    steer(N, 0);
  }

  drive(driveState, 255);
  
  delay(16); //60ups
}

void serialEvent(){
//statements
data = Serial.read();
}

void steer(int dir, int mph) {
  analogWrite(steerSpeed, mph);

  switch(dir) {
    case L:
      digitalWrite(steerA, 0);
      digitalWrite(steerB, 1);
      break;
    case R:
      digitalWrite(steerA, 1);
      digitalWrite(steerB, 0);
      break;
    case N:
      digitalWrite(steerA, 0);
      digitalWrite(steerB, 0);
      break;
  }
}

void drive(int dir, int mph) {
  analogWrite(driveSpeed, mph);

  switch(dir) {
    case F:
      digitalWrite(driveA, 0);
      digitalWrite(driveB, 1);
      digitalWrite(drive2A, 0);
      digitalWrite(drive2B, 1);
      break;
    case B:
      digitalWrite(driveA, 1);
      digitalWrite(driveB, 0);
      digitalWrite(drive2A, 1);
      digitalWrite(drive2B, 0);
      break;
    case N:
      digitalWrite(driveA, 0);
      digitalWrite(driveB, 0);
      digitalWrite(drive2A, 0);
      digitalWrite(drive2B, 0);
      break;
  }
}

