import org.testng.annotations.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

import io.github.bonigarcia.wdm.WebDriverManager;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class MedicureTest {

    @Test
    public void openWebsite() throws IOException {

        System.out.println("Setting up Chrome driver...");

        WebDriverManager.chromedriver().setup();

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless=new");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");

        WebDriver driver = new ChromeDriver(options);

        System.out.println("Opening MediCure website...");

        driver.get("https://medicure-enhanced.onrender.com");

        System.out.println("Page Title: " + driver.getTitle());
        System.out.println("Current URL: " + driver.getCurrentUrl());

        System.out.println("Taking screenshot...");

        File screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);

        File destination = new File("medicure_screenshot.png");

        Files.copy(screenshot.toPath(), destination.toPath(), StandardCopyOption.REPLACE_EXISTING);

        System.out.println("Screenshot saved as medicure_screenshot.png");

        driver.quit();

        System.out.println("Test completed successfully.");
    }
}