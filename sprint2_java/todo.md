# Todo
* use while and keep asking until an user type quit
* use a function inside of if, else if after an user type numbers corresponding weight, temp, length




### Sudo Code
1. ask users to quit or continue 
- if quit, break the while loop and tell bye bye 
- if continue, show measurements list.

``` java
for (int i = 0; i < weight.size(); i++) {
  System.out.println("----- Result: " + value + " " + selected + " => " + value*w_multiplier_kg.get(i) + " " + weight.get(i) + " -----");
}
for (int i = 0; i < weight.size(); i++) {
  float result = value*w_multiplier_kg.get(i);
  System.out.println("----- Result: " + value + " " + selected + " => " + String.format("%.2f", result) + " " + weight.get(i) + " -----");
}

show_result(weight, value, w_multiplier_kg, selected);
static void show_result(ArrayList<String> list, float value, ArrayList<Float> multiplier, String selected){
  for (int i = 0; i < list.size(); i++) {
    float result = value*multiplier.get(i);
    System.out.println("----- Result: " + value + " " + selected + " => " + String.format("%.2f", result) + " " + list.get(i) + " -----");
  }
}
```
