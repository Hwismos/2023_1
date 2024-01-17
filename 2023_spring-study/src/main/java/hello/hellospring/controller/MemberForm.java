package hello.hellospring.controller;

public class MemberForm {
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // spring이 setName을 호출해서 name을 세팅한다.
    private String name;
}
