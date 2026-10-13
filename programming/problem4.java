import java.util.ArrayList;

class User{
    String name;
    int age;

    User(String name, int age){
        this.name = name;
        this.age = age;
    }
}

public class problem4 {

    public static void main(String[] args) {
        
        ArrayList<User> users = new ArrayList<>();

        users.add(new User("A", 25));
        users.add(new User("B", 17));
        users.add(new User("C", 30));

        ArrayList<User> adults = new ArrayList<>();

        for (User user : users) {
            if (user.age > 18) {
                adults.add(user);
            }
        }

        // Printing User above age 18
        System.out.println("Users above 18 :");
        for(User adult : adults){
            System.out.println(adult.name + " : " + adult.age);
        }
    }
}