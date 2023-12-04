-- our database name is yoyo
use yoyo;

INSERT INTO clubbing_club (city_id, name, address, contact_info, type)
VALUES (1, 'Irish', 'Plaza Mayor', 'None', 'Nightclub')

INSERT INTO clubbing_club (city_id, name, address, contact_info, type)
VALUES 
(1, 'La Mentira', 'Plaza Mayor', 'None', 'Nightclub'),
(1, 'Kotaho Clubs', 'Plaza Mayor', 'None', 'Nightclub'),
(1, 'Sabat', 'Plaza Mayor', 'None', 'Nightclub'),
(1, 'La Luna', 'Plaza Mayor', 'None', 'Nightclub');

INSERT INTO clubbing_event (city_id, name, description, date_time)
VALUES
(1, 'Tankers Event', 'Techno', '2023-12-02 23:00:00'),
(1, 'Sense Segovia', 'Commercial', '2023-12-02 23:00:00'),
(1, 'Latino Party', 'Bad Bunny Music', '2023-12-02 23:00:00');

