package cn.itcast.c_property;

public class UserAction {

	// Service: springIOC����ע��
	private UserService userService;
	public void setUserService(UserService userService) {
		this.userService = userService;
	}
	

	public String execute() {
		userService.save();
		return null;
	}
}








