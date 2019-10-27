const int in_1 = 2 ;
const int in_2 = 3 ;
const int in_3 = 11 ;
const int in_4 = 12 ;


void setup()
{
pinMode(in_1,OUTPUT) ;
pinMode(in_2,OUTPUT) ;
pinMode(in_3,OUTPUT) ;
pinMode(in_4,OUTPUT) ;
}

void loop()
{

digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;

}
