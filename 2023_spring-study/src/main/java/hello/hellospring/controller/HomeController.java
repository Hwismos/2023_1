package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    @GetMapping("/")
    // 도메인에 들어오면 home.html이 렌더링 된다.
    // index.html이 렌더링되지 않는 이유는 우선순위가 있기 때문이다.
        // 정적 리소스는 우선순위가 낮다.
    public String home() {
        return "home";
    }
}
