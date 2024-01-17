package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;


/*
@Service  // → 컴포넌트 스캔 방법 → 스프링 빈으로 등록된다.
// 스프링이 멤버 서비스를 등록해준다.
// 순수한 자바 클래스 코드이므로 스프링이 컨테이너에 빈으로 등록해줄 필요가 있다.
 */

// 비즈니스 로직

@Transactional
public class MemberService {
    private final MemberRepository memberRepository;

    /*
    @Autowired
    // 생성자를 이용해 리포지토리를 초기화해준다.
    // 컴포넌트 스캔 방법은 기본적으로 싱글톤으로 동작한다.
    // 따라서, 각 스프링 빈은 공유될 수 있다.
     */
    public MemberService(MemberRepository memberRepository) {

        this.memberRepository = memberRepository;
    }

    // 회원가입
    // 같은 이름을 갖는 회원이 있으면 안된다.
    public Long join(Member member) {
//        Optional<Member> result = memberRepository.findByName(member.getName());
        // Optional 클래스 덕분에 사용할 수 있다.
        // null이 아니면 동작하는 함수
//        result.ifPresent(m -> {
//            throw new IllegalStateException("이미 존재하는 회원입니다.");
//        });
        validateDuplicatedMember(member);
        // 회원이 중복되지 않으면 저장한다.
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicatedMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    // 서비스 클래스는 네이밍(느낌)이 비즈니스에 가깝다. → 비즈니스 의존적
    // 리포지토리는 상대적으로 개발자에 친화적으로 네이밍을 잡는다.
    // 개발자나 기획자든 소통이 쉬워진다.
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }

}
