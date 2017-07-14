# -*- coding: UTF-8 -*-

class Student
    @@student_number=0
    #选取一些姓和名字用来随机生成学生姓名
    $familyNames=["张","王","赵","李","段","江","杨","孙","周","夏","崔","慕容","萧","乔","韩","苏"]
    $firstNames=["婷","誉","峰","无忌","敏","芷若","逊","逍","语嫣","复","博","远山","云","雨","飞","亮"]

    @age
    @name
    @gender
    @id
    def getAge()
    	@age=rand(15..20)
    	return @age
    end
    def getName()
    	@name=$familyNames.at(rand(0..15))+$firstNames.at(rand(0..14))
    	return @name
    end
    def getGender()
    	if rand(0..1)==0
    		@gender="男"
    		return @gender
    	else
    		@gender="女"
    		return @gender
    	end
    end
    def setId(id)
	    @id=id
    end
    def getId
	    return @id
    end
    def toString
    	"姓名："+self.getName+" \tid：#{self.getId}"+"\t性别："+self.getGender+" 年龄：#{self.getAge}"
    end
end
 if !File.file?( "student.txt" )
 	id=1
	stuFile = File.open("student.txt", "w")
	while id<=100
		stu=Student.new
		stu.setId(id)
		id+=1
		stuFile.syswrite(stu.toString+"\n")
	end
 else
 	stuFile = File.open("student.txt", "r")
 	line=1
 	while line<=100
 		puts stuFile.gets()
 		line=line+1
 	end
 end
