Switch/case example

Switch/case example

```java
public class Test {
    public var getMonthNumber() {
        return monthNumber = 2;
    }

    public void main(String[] args){
        String monthName = switch(monthNumber){
          case 1 -> "January";
          case 2 -> "February";
          case 3, 4, 5 -> "Spring";
          // Rest of cases
          default -> "unknown";
        };
    }
}
```

```java
String str;
int monitorInchSize = 24;
switch (monitorInchSize){
	case 15:
		str = "too small";
		break
	case 16: case 17: case 18:
		str = "good for the past decade";
		break;
	case 19: case 20: case 21: case 22: case 23:
		str = "for the office work";
		break;
	case 24: case 25: case 26: case 27:
		str = "great choice";
		break;
	default:
		str = "";
}
```

Result of the last example str = "great choice"