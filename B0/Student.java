import java.util.Random;

public class Student {
	String id;
	String name;
	String gender;
	int age;
	//随便找了一些姓和名字放在数组中用来随机生成学生姓名
	String[] familyNames={"张","王","赵","李","段","江","杨","孙","周","夏","崔","慕容","萧","乔","韩","苏"};
	String[] firstName={"婷","誉","峰","无忌","敏","芷若","逊","逍","语嫣","复","博","远山","云","雨","飞","亮"};
	public int getAge(){
		return (int)(Math.random()*5)+15;
	}
	public String getGender(){
		int a=(int)(Math.random()*2);
		if(a>1)
			return "男";
		else
			return "女";
	}
	public String getName(){
		return familyNames[(int)(Math.random()*familyNames.length)]+firstName[(int)(Math.random()*firstName.length)];		
	}
	public Student(int id){
		this.id=""+id;
		this.age=getAge();
		this.name=getName();
		this.gender=getGender();
	}
	public String toString(){
		return "id:"+this.id+" 姓名："+this.name+" 性别:"+this.gender+" 年龄："+this.age;
	}
}
