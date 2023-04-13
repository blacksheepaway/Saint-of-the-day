# Saint of the Day

Welcome to the Saint of the Day project! This application allows users to discover information about the saint of the day, providing a daily source of inspiration and learning about Catholic saints. The application fetches data from the Canção Nova website and presents it in an easy-to-read popup format. It's a great project to showcase your skills with web scraping, regular expressions, and GUI development in Python.

## How it Works

The Saint of the Day application retrieves the saint's name, image, image caption, and description from the Canção Nova website, focusing on the saint's feast day. It uses the `requests` library to fetch the webpage's content and `BeautifulSoup` to parse the HTML, extract the relevant data, and reformat it for display. The user interface is built using `PySimpleGUI`.

## Technologies and Techniques

- Python
- Web scraping with `requests` and `BeautifulSoup`
- Regular expressions for text manipulation
- `PySimpleGUI` for creating the graphical user interface
- File handling for temporary image storage

## Example

When the Saint of the Day application is run, it fetches information about the saint whose feast day it is and presents the data in a well-formatted popup window. The popup displays the date, saint's name, image, image caption, and description.

<p align="center">
  <img src="https://i.imgur.com/VJtVc4n.jpeg" width="350" title="hover text">
  <img src="https://i.imgur.com/EaN9s6l.png" width="350" alt="accessibility text">
</p>

## Modification for Other Applications

The Saint of the Day application can be easily modified for various purposes. For example, you could:

- Display information about saints with different criteria, such as alphabetically or by country
- Create a calendar application that includes feast days and other significant events in the Catholic liturgical year
- Integrate the project with a notification system to send daily reminders or emails with the saint's information

## Contribution

Contributions to improve or expand the project are highly appreciated. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add a new feature'`)
4. Push your branch to your fork (`git push origin feature-branch`)
5. Create a pull request

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify, and distribute the code as long as the license terms are met.
