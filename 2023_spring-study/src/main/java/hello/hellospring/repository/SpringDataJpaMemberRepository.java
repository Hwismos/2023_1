package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

// Spring 빈을 자동으로 만들어준다.
public interface SpringDataJpaMemberRepository extends JpaRepository<Member, Long>, MemberRepository {
    // JPQL select m from Member m where m.name = ?
    // 인터페이스 이름만으로도 개발이 끝난다.
    // 단순한 80%는 인터페이스만으로 끝이 난다.
    @Override
    Optional<Member> findByName(String name);

}
