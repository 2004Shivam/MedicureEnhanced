import org.testng.annotations.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import io.github.bonigarcia.wdm.WebDriverManager;

public class MedicureTest {

@Test
public void openWebsite() {

WebDriverManager.chromedriver().setup();

ChromeOptions options = new ChromeOptions();
options.addArguments("--headless=new");
options.addArguments("--no-sandbox");
options.addArguments("--disable-dev-shm-usage");

WebDriver driver = new ChromeDriver(options);

driver.get("https://medicureenhanced.onrender.com");

System.out.println("Page Title: " + driver.getTitle());

driver.quit();

}

}