#define EN        8      //Stepper Motor Enable, Active Low Level 
#define X_DIR    5      //X-Axis Stepper Motor Direction Control 
#define Y_DIR    6     //Y-Axis Stepper Motor Direction Control 
#define X_STP    2    //X-Axis Stepper Control 
#define Y_STP   3    //Y-Axis Stepper Control

#define VRX_PIN  A1 // Arduino pin connected to VRX pin
#define VRY_PIN  A0 // Arduino pin connected to VRY pin
#define SW_PIN   13  // Arduino pin connected to SW  pin

int dirx =0;
int stepss = 50;
int stepsl = 10;
char chardir;
int diry = 0;

int xValue = 0; // To store value of the X axis
int yValue = 0; // To store value of the Y axis
int bValue = 0; // To store value of the button

uint8_t btn_prev;
boolean joymove = false;

void step(boolean dir, byte dirPin, byte stepperPin, int steps)
{
  digitalWrite(dirPin, dir);
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(800);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(800);
  }
  delayMicroseconds(100);
}


void setup() {
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT); 
  pinMode(Y_STP, OUTPUT);
  pinMode(SW_PIN, INPUT_PULLUP);
  btn_prev = digitalRead(SW_PIN);
  pinMode(EN, OUTPUT);
  digitalWrite(EN, HIGH);
  Serial.begin(2000000);
}

void loop() {
  uint8_t btn = digitalRead(SW_PIN);
  if (btn == LOW && btn_prev == HIGH){
    joymove = !joymove;
    Serial.print("button pressed");
    delayMicroseconds(1500);
  }
  btn_prev = digitalRead(SW_PIN);

  if(joymove) {
    xValue = analogRead(VRX_PIN);
    yValue = analogRead(VRY_PIN);

    if (yValue > 750) {
      digitalWrite(EN, LOW);
      diry = 1;
      Serial.print("going up");
    } else if (yValue < 250) {
      digitalWrite(EN, LOW);
      diry = -1;
      Serial.print("going down");
    } else {
      diry = 0;
    }

    if (xValue > 750) {
      digitalWrite(EN, LOW);
      dirx = 1;
      Serial.print("going right");
    } else if (xValue < 250) {
      digitalWrite(EN, LOW);
      dirx = -1;
      Serial.print("going left");
    } else {
      dirx = 0;
    }

    if (dirx == 0 and diry == 0) {
      digitalWrite(EN, HIGH);
    }
    
  }
  
  if (Serial.available() and !joymove) {
//    chardir = (Serial.readString()).charAt(0);
    chardir = Serial.read();
    // Code for Camera Mode
    if (chardir == 'L') {
      digitalWrite(EN, LOW);
      dirx = -1;
      chardir = 'N';
    }
    else if (chardir == 'R') {
      digitalWrite(EN, LOW);
      dirx = 1;
      chardir = 'N';
    }
    else if (chardir == 'U') {
      digitalWrite(EN, LOW);
      diry = -1;
      chardir = 'N';
    }
    else if (chardir == 'D') {
      digitalWrite(EN, LOW);
      diry = 1;
      chardir = 'N';
    }
    else if (chardir == 'X') {
      digitalWrite(EN, LOW);
      dirx = 0;
      chardir = 'N';
    }
    else if (chardir == 'Y') {
      digitalWrite(EN, LOW);
      diry = 0;
      chardir = 'N';
    }

    // Stop all if nothing
    if ((((dirx == 0) && (diry == 0)) || (chardir == 'S')|| (chardir == 's'))) {
      digitalWrite(EN, LOW);
      dirx = 0;
      diry = 0;
      chardir = 'N';
    }
    
    // Stop hard stop
    if (chardir == 'E') {
      digitalWrite(EN, HIGH);
      dirx = 0;
      diry = 0;
      chardir = 'N';
    }
  }

  // Moving the platform
  if (dirx == -1) {
    step(false, X_DIR, X_STP, stepsl);
  }
  if (dirx == 1) {
    step(true, X_DIR, X_STP, stepsl);
  }
  if (diry == -1) {
    step(false, Y_DIR, Y_STP, stepsl);
  }
  if (diry == 1) {
    step(true, Y_DIR, Y_STP, stepsl);
  }
}
