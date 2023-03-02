# typo fix in the file wp-settings.php
exec { 'bug-fix':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
