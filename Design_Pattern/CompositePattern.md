# Composite Pattern(복합체 패턴)

- **컴포지트 패턴(Composite pattern)**이란 객체들의 관계를 트리 구조로 구성하여 부분-전체 계층을 표현하는 패턴으로, 사용자가 단일 객체와 복합 객체 모두 동일하게 다루도록 함.
- 컴포지트 패턴은 Component, Composite, Leaf 들로 구성됨.
- 그룹 전체와 개별 객체를 동일하게 처리할 수 있는 패턴
- 클라이언트 입장에서는 '전체'나 '부분'이나 모두 동일한 컴포넌트로 인식할 수 있는 계층 구조를 만든다. (Part-Whole Hierarchy)
![image](https://github.com/gijeogiya/TIL/assets/97646078/3ae3e972-06b7-47dd-9ba4-bcdd436115ef)
![image](https://github.com/gijeogiya/TIL/assets/97646078/4f9cbc52-e1d3-4293-8b9e-3a0bf223128d)




## 예시 코드

```java
import java.util.ArrayList;

public interface FileSystem {
  public int getSize();
  public void remove();
}

class File implements FileSystem {
  private String name;
  private int size;

  public File (String _name, int _size) {
    name = _name; size = _size;
  }

  @Override
  public int getSize() {
    System.out.println(name + "파일 크기 : " + size);
    return size;
  }

  @Override
  public void remove() {
    System.out.println(name + " 파일 삭제");
  }

}

class Folder implements FileSystem {
  private String name;
  private ArrayList<FileSystem> includeds = new ArrayList<>();

  public Folder (String _name) {
    name = _name;
  }

  public void add(FileSystem fileSystem) {
    includeds.add(fileSystem);
  }

  @Override
  public int getSize() {
    int total = 0;
    for (FileSystem included : includeds) {
      total += included.getSize();
    }
    System.out.println(name + "폴더 크기 : " + total);
    System.out.println("- - - - -");
    return total;
  }

  @Override
  public void remove() {
    for (FileSystem included : includeds) {
      included.remove();
    }
    System.out.println(name + " 폴더 삭제");
    System.out.println("- - - - -");
  }
}
```

```java
public class CompositePattern {
  public static void main(String[] args) {
    Folder schoolFolder = new Folder("학교");

    Folder grade1Folder = new Folder("1학년");
    Folder grade2Folder = new Folder("2학년");

    schoolFolder.add(grade1Folder);
    schoolFolder.add(grade2Folder);

    File enterPhoto = new File("입학사진", 256);
    grade1Folder.add(enterPhoto);

    Folder sem1Folder = new Folder("1학기");
    Folder sem2Folder = new Folder("2학기");

    grade2Folder.add(sem1Folder);
    grade2Folder.add(sem2Folder);

    File lecturePlan = new File("강의계획서", 120);
    sem1Folder.add(lecturePlan);

    Folder projFolder = new Folder("프로젝트");
    sem2Folder.add(projFolder);

    File draft = new File("드래프트", 488);
    File finalResult = new File("결과물", 560);

    projFolder.add(draft);
    projFolder.add(finalResult);

    schoolFolder.getSize();
    // 입학사진파일 크기 : 256
    // 1학년폴더 크기 : 256
    // - - - - -
    // 강의계획서파일 크기 : 120
    // 1학기폴더 크기 : 120
    // - - - - -
    // 드래프트파일 크기 : 488
    // 결과물파일 크기 : 560
    // 프로젝트폴더 크기 : 1048
    // - - - - -
    // 2학기폴더 크기 : 1048
    // - - - - -
    // 2학년폴더 크기 : 1168
    // - - - - -
    // 학교폴더 크기 : 1424
    // - - - - -

    schoolFolder.remove();
    // 입학사진 파일 삭제
    // 1학년 폴더 삭제
    // - - - - -
    // 강의계획서 파일 삭제
    // 1학기 폴더 삭제
    // - - - - -
    // 드래프트 파일 삭제
    // 결과물 파일 삭제
    // 프로젝트 폴더 삭제
    // - - - - -
    // 2학기 폴더 삭제
    // - - - - -
    // 2학년 폴더 삭제
    // - - - - -
    // 학교 폴더 삭제
    // - - - - -
  }
}
```



## 장단점

### 장점

- 그룹핑 : 단일 객체와 복합 객체(그룹)를 동일하게 여기기 때문에 묶어서 연산하거나 관리할 때 편하다.
- 복잡한 트리 구조를 편리하게 사용할 수 있다.
- 다형성과 재귀를 활용할 수 있다.
- 클라이언트 코드를 변경하지 않고 새로운 엘리먼트 타입을 추가할 수 있다.
### 단점

- 디버깅 어려움 : 재귀호출의 특징 상 트리의 Depth가 깊어질 수록 라인 단위의 디버깅에 어려움이 생긴다.
트리를 만들어야 하기 때문에 (공통된 인터페이스를 정의해야 하기 때문에) 지나치게 일반화 해야 하는 경우도 생길 수 있다.

## 실무에서 어떻게 쓰이나?
- Java
  - Swing 라이브러리
  - JSF (JavaServer Faces) 라이브러리
