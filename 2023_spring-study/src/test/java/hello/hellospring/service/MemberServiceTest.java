package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

// test 패키지 밑에 똑같이 만들어진다. (단축키 사용)
// 테스트는 한글로 네이밍을 해도 된다.
class MemberServiceTest {

    MemberService memberService;

    // static 이라 지금은 상관 없지만 static이 아니면 새로 객체를 생성하는 것은 다른 DB를 테스트 하는 것이므로 문제가 있다.
    MemoryMemberRepository memberRepository;

    @BeforeEach
    // 외부에서 멤버리포지토리를 넣어준다. → 같은 멤버리포지토리를 사용한다.
    // DI(Dependency Injection)
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }

    @Test
    void 회원가입() {
        // given → "이 데이터를 이용하는구나!"
        Member member = new Member();
        member.setName("hello");

        // when → "이걸 검증하는구나!"
        // 리포지토리에 정상적으로 저장되었는지를 확인한다.
        Long savedId = memberService.join(member);

        // then → "여기가 검증부구나!"
        // get 메소드를 사용하지 않으면 반환 타입을 Optional로 감싸줘야 한다.
        Member findMember = memberService.findOne(savedId).get();
        Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    // 테스트는 예외 흐름을 찾는 것이 더 중요하다.
    @Test
    public void 중복_회원_예외() {
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        memberService.join(member1);

        // 오른쪽에 로직이 들어간다.
        // member2를 넣으면 예외가 터져야 한다.
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2)); // cmd + alt + V
        Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

        // 이름이 똑같은 회원이 들어갔다. → 예외가 터져야 한다.
//        try {
//            memberService.join(member2);
//            fail();
//        } catch (IllegalStateException e) {
//            // 예외가 터지면 이 구문으로 들어온다.
//            // 정상적이다.
//            Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
//        }

        // then

    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}