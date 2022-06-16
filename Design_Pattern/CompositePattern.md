# Composite Pattern

- **컴포지트 패턴(Composite pattern)**이란 객체들의 관계를 트리 구조로 구성하여 부분-전체 계층을 표현하는 패턴으로, 사용자가 단일 객체와 복합 객체 모두 동일하게 다루도록 함.

- 컴포지트 패턴은 Component, Composite, Leaf 들로 구성됨.

  

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

