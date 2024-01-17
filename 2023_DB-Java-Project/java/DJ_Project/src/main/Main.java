package main;

import java.sql.*;

public class Main {

	public static void main(String[] args) {
		try {
			// db에 접속
			// jdbc:Driver 종류: //IP포트번호/DB명
			Connection conn = DriverManager.getConnection(
					"jdbc:mysql://localhost:3306/?user=company", 
					"root",
					"712476"
					);
			System.out.println("success\n");
			
			// db에 명령어를 전달할 수 있는 객체 생성
			Statement stmt = conn.createStatement();
			ResultSet rs = stmt.executeQuery("select eno from employee");
			while(rs.next()) {				
				System.out.println(rs.getString("eno"));
			}
			
			
		} catch(SQLException e) {
			System.out.println("SQLException: " + e);
		}
	}

}
