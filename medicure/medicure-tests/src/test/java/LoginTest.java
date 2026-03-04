import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class LoginTest {

    @Test
    public void openMedicureWebsite() {

        WebDriver driver = new ChromeDriver();

        driver.get("https://your-medicure-url.onrender.com");

        System.out.println("Page Title: " + driver.getTitle());

        driver.quit();
    }
}