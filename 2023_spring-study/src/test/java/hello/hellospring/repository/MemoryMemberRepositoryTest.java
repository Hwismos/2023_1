package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

// 모든 테스트는 순서와 독립적이다.
// 따라서 순서에 의존적으로 설계하면 안된다.
// ★★ 테스트가 끝날 때마다 테스트 데이터를 클리어 해줘야 한다.

// 검증할 수 있는 틀을 만들고 실제로 구현하는 클래스를 만드는 방법을 '테스트 주도 개발(TDD)' 이라고 한다.
// 테스트 관련해서 깊이 있게 공부할 것을 권장한다.
public class MemoryMemberRepositoryTest {
    MemoryMemberRepository repository = new MemoryMemberRepository();

    // 콜백 메소드와 같다.
    // 각 메소드가 끝날 때마다 호출된다.
    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);
        // findById가 Optional 타입을 반환하므로 get으로 꺼내준다.
        Member result = repository.findById(member.getId()).get();
//        System.out.println("result = " + (result == member));
        // 같으면 아무런 것이 안 뜬다.
//        Assertions.assertEquals(member, result);
        // member가 result와 동일한지를 가독성 높게 표현할 수 있다.
        assertThat(member).isEqualTo(result);

        // 실무에서는 build tool과 엮어서 오류가 있으면 다음 단계로 넘어가지 못하도록 한다.
    }

    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        // fingByName 메소드가 정상적으로 동작하는지 확인한다.
        Member result = repository.findByName("spring1").get();
        assertThat(result).isEqualTo(member1);
    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();
        assertThat(result.size()).isEqualTo(2);
    }
}
