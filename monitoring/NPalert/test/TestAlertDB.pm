package test::TestAlertDB;

use strict;

use base qw(Test::Unit::TestCase);

use NOCpulse::Notif::AlertDB;
use NOCpulse::Log::Logger;
my $Log = NOCpulse::Log::Logger->new(__PACKAGE__,9);

my $MODULE = 'NOCpulse::Notif::AlertDB';

$| = 1;

######################
sub test_constructor {
######################
  my $self = shift;
  my $obj = $MODULE->new();

  # Make sure creation succeeded
  $self->assert(defined($obj), "Couldn't create $MODULE object: $@");

  # Make sure we got the right type of object
  $self->assert(qr/$MODULE/, "$obj");
        
}

############
sub set_up {
############
  my $self = shift;
  # This method is called before each test.

  $self->{'blah'}=$MODULE->new();
}

###############
sub tear_down {
###############
  my $self = shift;
  $self->{'blah'}->disconnect;
}

# INSERT INTERESTING TESTS HERE

##################
sub test_general {
##################
  my $self=shift;
  $self->{'blah'}->dbprepare('test','select 29 as x from dual');
  my ($err,$arrayref)=$self->{'blah'}->dbexecute('test');
  if ($err) {
    $Log->log(1,"err: $arrayref\n");
    $self->assert(!$err);
  } else {
    $Log->dump(1,"\narray: ",$arrayref,"\n");
    my $value=shift(@$arrayref);
    $value=shift(@$value);
    $Log->dump(1,"\nvalue: ",$value,"\n");
    $self->assert($value == 29);
  }
}

sub test_dbexecute {
  # See test_alert
}

################
sub test_alert {
################
  my $self=shift;
  $Log->log(1,"create\n");
  my ($err)=$self->{'blah'}->dbexecute('create_current_alert',  3, undef, 'message', '01_1031071399_011923_006', 'destination_name',0, 1, 'down', '2', 'up', 30, 10, 'service_probe', '28/10/2000 10:00:00');
  $self->assert($err==0,$err);
  $Log->log(1,"escalate\n");
  ($err)=$self->{'blah'}->dbexecute('escalate_current_alert','03_1031071399_011923_006','03_1031071399_011923_006');
  $self->assert($err==0,$err);
  $Log->log(1,"clear\n");
  ($err)=$self->{'blah'}->dbexecute('clear_alert','03_1031071399_011923_006');
  $self->assert($err==0,$err);
}

############################
sub test_create_snmp_alert {
############################
  my $self=shift;
  my ($err)=$self->{'blah'}->dbexecute('create_snmp_alert',10068, 'dave.pc.nocpulse.net', 
                                       5050, '10-09-2002 20:46:23', '10-09-2002 20:46:23',
                                       'Disk Space', 1, 'NOCpulse Lab', 'https://command.nocpulse.com/ocenter/?function=host&id=19231',
                                       'Spacewalk','message: Filesystem /dev/hda2: Filesystem pct used 35% (above critical threshold of 20%); Space available 1,115 MB; Space used 591 MB 
								  Notification #1413 for Filesystem pct used',
                                       20080, '192.168.0.234',1, 
				       17, 1, 'VMWare4');
  $self->assert($err==0,$err);
}

#######################
sub test_redirect_seq {
#######################
  my $self=shift;
  my ($one,$two);
  my ($err,$arrayref)=$self->{'blah'}->dbexecute('select_next_redirect_recid');
  my ($err2,$arrayref2)=$self->{'blah'}->dbexecute('select_next_redirect_recid');
  if ($err) {
    $Log->log(1,"err: $arrayref\n");
    $self->assert(!$err,'err');
  } else {
    $Log->dump(1,"\narray: ",$arrayref,"\n");
    my $value=shift(@$arrayref);
    $one=shift(@$value);
    $Log->dump(1,"\nvalue: ",$one,"\n");
  }
  if ($err2) {
    $Log->log(1,"err2: $arrayref2\n");
    $self->assert(!$err2,'err2');
  } else {
    $Log->dump(1,"\narray: ",$arrayref2,"\n");
    my $value=shift(@$arrayref2);
    $two=shift(@$value);
    $Log->dump(1,"\nvalue: ",$two,"\n");
  }
  $self->assert($two == $one + 1,"sequence");
}

####################
sub test_redirects {
####################
  my $self=shift;
  my ($err,$arrayref)=$self->{'blah'}->dbexecute('select_next_redirect_recid');
  my $value=shift(@$arrayref);
  my $one=shift(@$value);

  ($err)=$self->{'blah'}->dbexecute('create_redirect',$one,30,454,'METOO','test redirects','test program','01-01-2003 00:00:00','01-01-2003 00:00:01','testpgm');

  $self->assert(!$err,'create_redirect');

  ($err)=$self->{'blah'}->dbexecute('create_redirect_criterion',$one,'PROBE_ID',1);
  $self->assert(!$err,'create_redirection');

  ($err)=$self->{'blah'}->dbexecute('create_redirect_email_target',$one,'nobody@nocpulse.com');
  $self->assert(!$err,'create_redirect_email_target');

  ($err)=$self->{'blah'}->dbexecute('delete_redirect_email_targets',$one);
  $self->assert(!$err,"delete_redirect_email_targets $err");

  ($err)=$self->{'blah'}->dbexecute('delete_redirect_criteria',$one);
  $self->assert(!$err,'delete_redirect_criteria');

  ($err)=$self->{'blah'}->dbexecute('delete_redirect',$one);
  $self->assert(!$err,'delete_redirect');
}

sub test_connected {
  #See test_connect
}

sub test_disconnect {
  #See test_connect
}

sub test_dbprepare {
  #See test_connect
}

##################
sub test_connect {
##################
  my $self = shift;
  my $db = $self->{'blah'};

  $db->connect;

  eval {
    $db->dbprepare("select * from dual");
  };

  $self->assert(!$@,"connect");
  $self->assert($db->connected, "connected");
  
  $db->disconnect;
  $self->assert(!$db->connected, "not connected");
  
}

sub test_init_statements {
  my $self = shift;
  my $db = $self->{'blah'};
  $db->connect;

  my @values=$db->statements_values;
  my $size=scalar(@values);

  $self->assert($size > 0, "test_init_statements");
}

1;
