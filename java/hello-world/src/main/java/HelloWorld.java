public class HelloWorld {
    public static String hello(String name) {
        if (name == "" || name == null) name = "World";
        return "Hello, " + name + "!";
    }
}
