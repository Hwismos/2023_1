package hello.hellospring.controller;

import hello.hellospring.domain.Member;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.awt.*;
import java.util.List;

@Controller
// 스프링 컨테이러라는 통이 생기며 MemberController를 컨테이너에 넣어둔다.
// 스프링 컨테이너에서 빈을 관리한다.
// 스프링 컨테이너는 스프링 부트에 포함된다.
// 멤버 서비스를 가져다 쓴다.
public class MemberController {
    // 멤버 서비스가 여러 곳에 쓰일 수 있다.
    // 스프링 컨테이너에 등록하는 방식으로 쓸 수 있다.
//    private final MemberService memberService;
    private MemberService memberService;

    @Autowired
    // setter 주입
    // setter가 public하게 노출된다는 점이 단점이다.
    public void setMemberService(MemberService memberService) {
        this.memberService = memberService;
    }

    @Autowired
    // 스프링이 멤버 서비스를 연결시켜준다.
    // 생성자를 이용한다.
    // 의존관계를 주입해주는 것(생성자 주입) → Dependency Injection
        // 애플리케이션 조립 시점에서만 생성자를 이용하고 동적으로 변동하지 않는다.
        // 실행 중에 동적으로 바뀌는 경우는 없고, 수정해서 서버를 다시 띄운다.
    // 필드 주입은 권장되지 않는다.
    // SpringConfig(자바 코드로 스프링 빈 등록)를 이용해도 Controller에서는 Autowired 어노테이션을 붙여준다.
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    // 조회할 때 get을 쓴다.
    public String createForm() {
        // 아래의 html로 이동, 템플릿에서 찾는다.
        // 뷰 리졸버에 의해 선택되어 렌더링 된다.
        // form 태그는 값을 입력할 수 있는 태그다.
        return "members/createMemberForm";
    }

    @PostMapping("/members/new")
    // 데이터를 form에 넣어서 전달할 때 사용한다.
    public String create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());

        System.out.println(member.getName());

        memberService.join(member);

        return "redirect:/";
    }

    @GetMapping("/members")
    public String list(Model model) {
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members);
        return "members/memberList";
    }
}
