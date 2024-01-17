package hello.hellospring.domain;

import javax.persistence.*;

@Entity
// JPA가 관리하게 된다.
public class Member {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    // DB가 알아서 생성해준다.
    private Long id;    // 시스템이 저장하는 ID
    @Column(name = "name")
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
