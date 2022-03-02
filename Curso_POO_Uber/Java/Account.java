package github.platzi.CursoPOOUber.Java;

class Account {
    Integer id;
    String name;
    String document;
    String email;
    String password;

    public Account(String name, String document, String email, String password){
        this.name = name;
        this.document = document;
        this.email = email;
        this.password = password;
    }

    public Account(String name, String document){
        this.name = name;
        this.document = document;
    }
}