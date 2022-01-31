import java.util.Scanner;  // Import the Scanner class
import java.util.ArrayList;

class Main {
  public static Float show_measurements(ArrayList<String> list) {
    // for(String element : list) {
    //   System.out.println(element);
    // }
    System.out.println("Pick one below  you want to convert from and type the number. ");
    for(int i=0; i<list.size(); i++) {
      System.out.println((i+1) +". " + list.get(i));
    }
    Scanner obj = new Scanner(System.in);
    String measurements_which = obj.nextLine();
    System.out.println("Your pick => " + list.get(Integer.parseInt(measurements_which)-1));
    list.remove(Integer.parseInt(measurements_which)-1);
    while (true) {
      System.out.println("Type a number from 999.9 to -999.9: ");
      Scanner val_obj = new Scanner(System.in);
      float val_obj_to_float = val_obj.nextFloat();
      if (-999.9 <= val_obj_to_float && val_obj_to_float <= 999.9) {
        return val_obj_to_float;
      } else {
        error("----- Error: Invalid number -----");
      }
    }

  }
  static void error(String msg) {
    System.out.println(msg);
  }
  static void endMsg() {
    System.out.println("Thanks for using. Have a wonderful day!!");
  }

  public static void main(String[] args) {
    System.out.println("Welcome to a coverter app. ");
    
    while (true) {
      Scanner obj = new Scanner(System.in);  // Create a Scanner object
      System.out.println("Type one of the numbers. \n1. continue \n2. quit");
      String quit_continue = obj.nextLine();  // Read user input
      // Ask users to quit or convert
      if (quit_continue.equals("1")) {    
        
        while (true) {
          // Take an input from a user
          Scanner which = new Scanner(System.in);
          System.out.println("Which do you convert?? Type one of the numbers. \n1. weight \n2. temp \n3. length");
          String choice = which.nextLine();
          if (choice.equals("1")){
            ArrayList<String> weight = new ArrayList<>();
            weight.add("kg");
            weight.add("lbs");
            float value = show_measurements(weight);
            System.out.println(value);
            break;
          } else if (choice.equals("2")){
            ArrayList<String> temp = new ArrayList<>();
            temp.add("°C");
            temp.add("°F");
            show_measurements(temp);
            break;
          } else if (choice.equals("3")) {
            ArrayList<String> length = new ArrayList<>() {{
              add("inch");
              add("feet");
              add("cm");
            }};
            show_measurements(length);
            break;
          } else {
            error("----- Error: Invalid input. Type one of [weight, temp, length]. -----");
          }
        }
      } else if (quit_continue.equals("2")) {
        endMsg();
        break;
      } else {
        error("----- Error: Invalid input. Type either [continue, quit]. -----");
      }
    }
  }
}


// Scanner user = new Scanner(System.in);  // Create a Scanner object
// System.out.println("Enter username");
// String userName = user.nextLine();  // Read user input
// System.out.println("Hello, " + userName);  // Output user input