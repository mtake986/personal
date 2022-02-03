import java.util.Scanner;  // Import the Scanner class
import java.util.ArrayList;

class Main {
  public static String show_and_select_measurements(ArrayList<String> list) {
    // for(String element : list) {
    //   System.out.println(element);
    // }
    System.out.println("Pick one below  you want to convert from and type the number. ");
    for(int i=0; i<list.size(); i++) {
      System.out.println((i+1) +". " + list.get(i));
    }
    while(true) {
      Scanner obj = new Scanner(System.in);
      int measurements_num = obj.nextInt();
      if (1 <= measurements_num && measurements_num <= list.size()) {
        System.out.println("Your pick => " + list.get(measurements_num-1));
        String selected_measurement = list.get(measurements_num-1);
        list.remove(measurements_num-1);
        return selected_measurement;
      } else {
        error("----- Error: Invalid number -----");
      }
    }
  }
  public static float get_number(String selected) {
    while (true) {
      if (selected.equals("temp")) {
        System.out.println("Type a number from -999.9 to 999.9: ");
        Scanner val_obj = new Scanner(System.in);
        float val_obj_to_float = val_obj.nextFloat();
        if (-999.9 <= val_obj_to_float && val_obj_to_float <= 999.9) {
          return val_obj_to_float;
        } else {
          error("----- Error: Invalid number -----");
        }
      } else {
        System.out.println("Type a number from 0 to 99,999.9: ");
        Scanner val_obj = new Scanner(System.in);
        float val_obj_to_float = val_obj.nextFloat();
        if (0 <= val_obj_to_float && val_obj_to_float <= 999.9) {
          return val_obj_to_float;
        } else {
          error("----- Error: Invalid number -----");
        }
      }
    }
  }
  static void error(String msg) {
    System.out.println(msg);
  }
  static void endMsg() {
    System.out.println("Thanks for using. Have a wonderful day!!");
  }
  static void show_result(ArrayList<String> list, float value, ArrayList<Float> multiplier, String selected){
    for (int i = 0; i < list.size(); i++) {
      float result = value*multiplier.get(i);
      System.out.println("----- Result: " + value + " " + selected + " => " + String.format("%.2f", result) + " " + list.get(i) + " -----");
    }
  }

  public static void main(String[] args) {
    System.out.println("--------------------------------------");
    System.out.println("----- Welcome to a coverter app. -----");
    System.out.println("--------------------------------------");
    
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
            weight.add("oz");
            // get a selected measurement, value
            String selected = show_and_select_measurements(weight);
            float value = get_number("weight");
            // System.out.println("This is a list: " + weight);
            // System.out.println("This is a seleceted measurement: " + selected);
            // System.out.println("This is a value: " + value);
            switch (selected){
              case "kg":
                ArrayList<Float> w_multiplier_kg = new ArrayList<Float>() {{
                  add(2.2f);
                  add(35.27f);
                }};
                show_result(weight, value, w_multiplier_kg, selected);
                break;
              case "lbs":
                ArrayList<Float> w_multiplier_lbs = new ArrayList<Float>() {{
                  add(.45f);
                  add(16f);
                }};
                show_result(weight, value, w_multiplier_lbs, selected);
                break;
              case "oz":
                ArrayList<Float> w_multiplier_oz = new ArrayList<Float>() {{
                  add(0.0283f);
                  add(0.0625f);
                }};
                show_result(weight, value, w_multiplier_oz, selected);
                break;
            }
            break;
          } else if (choice.equals("2")){
            ArrayList<String> temp = new ArrayList<>();
            temp.add("°C");
            temp.add("°F");
            // get a selected measurement, value
            String selected = show_and_select_measurements(temp);
            float value = get_number("temp");
            switch (selected){
              case "°C":
                float temp_converted_value_to_f = value / 5 * 9 + 32;
                System.out.println("----- Result: " + value + selected + " => " + String.format("%.1f", temp_converted_value_to_f) + temp.get(0) + " -----");
                break;
              case "°F":
                float temp_converted_value_to_c = (value - 32 ) / 9 * 5;
                System.out.println("----- Result: " + value + selected + " => " + String.format("%.1f", temp_converted_value_to_c) + temp.get(0) + " -----");
                break;
            }
            break;
          } else if (choice.equals("3")) {
            ArrayList<String> length = new ArrayList<>() {{
              add("inch");
              add("feet");
              add("cm");
            }};
            // get a selected measurement, value
            String selected = show_and_select_measurements(length);
            float value = get_number("length");
            switch (selected){
              case "inch":
                ArrayList<Float> len_multiplier_in = new ArrayList<Float>() {{
                  add(.083f);
                  add(2.54f);
                }};
                show_result(length, value, len_multiplier_in, selected);
                break; 
              case "feet":
                ArrayList<Float> len_multiplier_ft = new ArrayList<Float>() {{
                  add(12f);
                  add(30.48f);
                }};
                show_result(length, value, len_multiplier_ft, selected);
                break;
              case "cm":
                ArrayList<Float> len_multiplier_cm = new ArrayList<Float>() {{
                  add(0.39f);
                  add(0.033f);
                }};
                show_result(length, value, len_multiplier_cm, selected);
                break;
            }
            break;
          } else {
            error("----- Error: Invalid number -----");
          }
        }
      } else if (quit_continue.equals("2")) {
        endMsg();
        break;
      } else {
        error("----- Error: Invalid number -----");
      }
      System.out.println("===============================================");
    }
  }
}


// Scanner user = new Scanner(System.in);  // Create a Scanner object
// System.out.println("Enter username");
// String userName = user.nextLine();  // Read user input
// System.out.println("Hello, " + userName);  // Output user input