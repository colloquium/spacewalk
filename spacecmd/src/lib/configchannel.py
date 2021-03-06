#
# Licensed under the GNU General Public License Version 3
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2010 Aron Parsons <aron@redhat.com>
#

# NOTE: the 'self' variable is an instance of SpacewalkShell

from optparse import Option
from spacecmd.utils import *

def help_configchannel_list(self):
    print 'configchannel_list: List all configuration channels'
    print 'usage: configchannel_list'

def do_configchannel_list(self, args, doreturn=False):
    channels = self.client.configchannel.listGlobals(self.session)
    channels = [c.get('label') for c in channels]

    if doreturn:
        return channels
    else:
        if len(channels):
            print '\n'.join(sorted(channels))

####################

def help_configchannel_listsystems(self):
    print 'configchannel_listsystems: List the systems subscribed to a'
    print '                           configuration channel'
    print 'usage: configchannel_listsystems CHANNEL'

def complete_configchannel_listsystems(self, text, line, beg, end):
    return tab_completer(self.do_configchannel_list('', True), text)

def do_configchannel_listsystems(self, args):
    if not self.check_api_version('10.11'):
        logging.warning("This version of the API doesn't support this method")
        return

    (args, options) = parse_arguments(args)

    if not len(args):
        self.help_configchannel_listsystems()
        return

    channel = args[0]

    systems = self.client.configchannel.listSubscribedSystems(self.session,
                                                              channel)

    systems = sorted([s.get('name') for s in systems])

    if len(systems):
        print '\n'.join(systems)

####################

def help_configchannel_listfiles(self):
    print 'configchannel_listfiles: List the files in a config channel'
    print 'usage: configchannel_listfiles CHANNEL ...'

def complete_configchannel_listfiles(self, text, line, beg, end):
    return tab_completer(self.do_configchannel_list('', True), text)

def do_configchannel_listfiles(self, args, doreturn=False):
    (args, options) = parse_arguments(args)

    if not len(args):
        self.help_configchannel_listfiles()
        return []

    for channel in args:
        files = self.client.configchannel.listFiles(self.session,
                                                    channel)
        files = [f.get('path') for f in files]

        if doreturn:
            return files
        else:
            if len(files):
                print '\n'.join(sorted(files))

####################

def help_configchannel_filedetails(self):
    print 'configchannel_filedetails: Show the details of a file'
    print 'in a configuration channel'
    print 'usage: configchannel_filedetails CHANNEL FILE [REVISION]'

def complete_configchannel_filedetails(self, text, line, beg, end):
    parts = line.split(' ')

    if len(parts) == 2:
        return tab_completer(self.do_configchannel_list('', True),
                                  text)
    elif len(parts) > 2:
        return tab_completer(\
            self.do_configchannel_listfiles(parts[1], True), text)
    else:
        return []

def do_configchannel_filedetails(self, args):
    (args, options) = parse_arguments(args)

    if len(args) < 2:
        self.help_configchannel_filedetails()
        return

    channel = args[0]
    filename = args[1]
    revision = None

    try:
        revision = int(args[2])
    except:
        pass

    # the server return a null exception if an invalid file is passed
    valid_files = self.do_configchannel_listfiles(channel, True)
    if not filename in valid_files:
        logging.warning('%s is not in this configuration channel' % filename)
        return

    if revision:
        details = self.client.configchannel.lookupFileInfo(self.session,
                                                           channel,
                                                           filename,
                                                           revision)
    else:
        results = self.client.configchannel.lookupFileInfo(self.session,
                                                           channel,
                                                           [ filename ])

        # grab the first item since we only do one file
        details = results[0]

    print 'Path:     %s' % details.get('path')
    print 'Type:     %s' % details.get('type')
    print 'Revision: %i' % details.get('revision')
    print 'Created:  %s' % details.get('creation')
    print 'Modified: %s' % details.get('modified')

    if details.get('type') == 'symlink':
        print
        print 'Target Path:     %s' % details.get('target_path')
    else:
        print
        print 'Owner:           %s' % details.get('owner')
        print 'Group:           %s' % details.get('group')
        print 'Mode:            %s' % details.get('permissions_mode')

    print 'SELinux Context: %s' % details.get('selinux_ctx')

    if details.get('type') == 'file':
        print 'MD5:             %s' % details.get('md5')
        print 'Binary:          %s' % details.get('binary')

        if not details.get('binary'):
            print
            print 'Contents'
            print '--------'
            print details.get('contents')

####################

def help_configchannel_details(self):
    print 'configchannel_details: Show the details of a config channel'
    print 'usage: configchannel_details CHANNEL ...'

def complete_configchannel_details(self, text, line, beg, end):
    return tab_completer(self.do_configchannel_list('', True), text)

def do_configchannel_details(self, args):
    (args, options) = parse_arguments(args)

    if not len(args):
        self.help_configchannel_details()
        return

    add_separator = False

    for channel in args:
        details = self.client.configchannel.getDetails(self.session,
                                                       channel)

        files = self.client.configchannel.listFiles(self.session,
                                                    channel)

        if add_separator: print self.SEPARATOR
        add_separator = True

        print 'Label:       %s' % details.get('label')
        print 'Name:        %s' % details.get('name')
        print 'Description: %s' % details.get('description')

        print
        print 'Files'
        print '-----'
        for f in files:
            print f.get('path')

####################

def help_configchannel_create(self):
    print 'configchannel_create: Create a configuration channel'
    print '''usage: configchannel_create [options]

options:
  -n NAME
  -d DESCRIPTION'''

def do_configchannel_create(self, args):
    options = [ Option('-n', '--name', action='store'),
                Option('-d', '--description', action='store') ]

    (args, options) = parse_arguments(args, options)

    if is_interactive(options):
        options.name = prompt_user('Name:', noblank = True)
        options.description = prompt_user('Description:')

        if options.description == '': options.description = options.name
    else:
        if not options.name:
            logging.error('A name is required')
            return

        if not options.description:
            options.description = options.name

    self.client.configchannel.create(self.session,
                                     options.name,
                                     options.name,
                                     options.description)

####################

def help_configchannel_delete(self):
    print 'configchannel_delete: Delete a configuration channel'
    print 'usage: configchannel_delete CHANNEL ...'

def complete_configchannel_delete(self, text, line, beg, end):
    return tab_completer(self.do_configchannel_list('', True), text)

def do_configchannel_delete(self, args):
    (args, options) = parse_arguments(args)

    if not len(args):
        self.help_configchannel_delete()
        return

    channels = args

    if self.user_confirm('Delete these channels [y/N]:'):
        self.client.configchannel.deleteChannels(self.session, channels)

####################

def help_configchannel_addfile(self):
    print 'configchannel_addfile: Create a configuration file'
    print '''usage: configchannel_addfile [CHANNEL] [options]

options:
  -c CHANNEL
  -p PATH
  -r REVISION
  -o OWNER [default: root]
  -g GROUP [default: root]
  -m MODE [defualt: 0644]
  -x SELINUX_CONTEXT
  -d path is a directory
  -s path is a symlink
  -t SYMLINK_TARGET
  -f local path to file contents'''

def complete_configchannel_addfile(self, text, line, beg, end):
    return tab_completer(self.do_configchannel_list('', True), text)

def do_configchannel_addfile(self, args, update_path=''):
    options = [ Option('-c', '--channel', action='store'),
                Option('-p', '--path', action='store'),
                Option('-o', '--owner', action='store'),
                Option('-g', '--group', action='store'),
                Option('-m', '--mode', action='store'),
                Option('-x', '--selinux-ctx', action='store'),
                Option('-t', '--target-path', action='store'),
                Option('-f', '--file', action='store'),
                Option('-r', '--revision', action='store'),
                Option('-s', '--symlink', action='store_true'),
                Option('-d', '--directory', action='store_true') ]

    (args, options) = parse_arguments(args, options)

    # initialize here instead of multiple times below
    contents = ''

    if is_interactive(options):
        # the channel name can be passed in
        if len(args):
            options.channel = args[0]
        else:
            while True:
                print 'Configuration Channels'
                print '----------------------'
                print '\n'.join(sorted(self.do_configchannel_list('', True)))
                print

                options.channel = prompt_user('Select:', noblank = True)

                # ensure the user enters a valid configuration channel
                if options.channel in self.do_configchannel_list('', True):
                    break
                else:
                    print
                    logging.warning('%s is not a valid channel' % \
                                    options.channel)
                    print

        if update_path:
            options.path = update_path
        else:
            options.path = prompt_user('Path:', noblank = True)

        # check if this file already exists
        try:
            fileinfo = \
                self.client.configchannel.lookupFileInfo(self.session,
                                                         options.channel,
                                                         [ options.path ])
        except:
            fileinfo = None

        # use existing values if available
        if fileinfo:
            for info in fileinfo:
                if info.get('path') == options.path:
                    logging.debug('Found existing file in channel')

                    options.owner = info.get('owner')
                    options.group = info.get('group')
                    options.mode = info.get('permissions_mode')
                    options.target_path = info.get('target_path')
                    options.selinux_ctx = info.get('selinux_ctx')
                    contents = info.get('contents')

                    if info.get('type') == 'symlink':
                        options.symlink = True

        if not options.owner: options.owner = 'root'
        if not options.group: options.group = 'root'
        if not options.mode: options.mode = '0644'

        # if this is a new file, ask if it's a symlink
        if not options.symlink:
            userinput = prompt_user('Symlink [y/N]:')
            if re.match('y', userinput, re.I):
                options.symlink = True
            else:
                options.symlink = False

        if options.symlink:
            target_input = prompt_user('Target Path:', noblank = True)
            selinux_input = prompt_user('SELinux Context [none]:')

            if target_input:
                options.target_path = target_input

            if selinux_input:
                options.selinux_ctx = selinux_input
        else:
            userinput = prompt_user('Directory [y/N]:')
            if re.match('y', userinput, re.I):
                options.directory = True
            else:
                options.directory = False

            owner_input = prompt_user('Owner [%s]:' % options.owner)
            group_input = prompt_user('Group [%s]:' % options.group)
            mode_input  = prompt_user('Mode [%s]:' % options.mode)
            selinux_input = \
                prompt_user('SELinux Context [%s]:' % options.selinux_ctx)
            revision_input  = prompt_user('Revision [next]:')

            if owner_input:
                options.owner = owner_input

            if group_input:
                options.group = group_input

            if mode_input:
                options.mode = mode_input

            if selinux_input:
                options.selinux_ctx = selinux_input

            if revision_input:
                try:
                    options.revision = int(revision_input)
                except:
                    logging.warning('The revision must be an integer')

            if not options.directory:
                if self.user_confirm('Read an existing file [y/N]:',
                                     nospacer = True, ignore_yes = True):
                    options.file = prompt_user('File:')
                    contents = read_file(options.file)
                else:
                    if contents:
                        template = contents
                    else:
                        template = ''

                    contents = editor(template = template, delete = True)
    else:
        if not options.path:
            logging.error('The path is required')
            return

        if not options.symlink and not options.directory:
            if options.file:
                contents = read_file(options.file)
            else:
                logging.error('You must provide the file contents')
                return

        if options.symlink and not options.target_path:
            logging.error('You must provide the target path for a symlink')
            return

    # selinux_ctx can't be None
    if not options.selinux_ctx:
        options.selinux_ctx = ''

    # directory can't be None
    if not options.directory:
        options.directory = False

    if options.symlink:
        file_info = { 'target_path' : options.target_path,
                      'selinux_ctx' : options.selinux_ctx }

        print 'Path:            %s' % options.path
        print 'Target Path:     %s' % file_info['target_path']
        print 'SELinux Context: %s' % file_info['selinux_ctx']
    else:
        if not options.owner: options.owner = 'root'
        if not options.group: options.group = 'root'
        if not options.mode:
            if options.directory:
                options.mode = '0755'
            else:
                options.mode = '0644'

        file_info = { 'contents'    : ''.join(contents),
                      'owner'       : options.owner,
                      'group'       : options.group,
                      'selinux_ctx' : options.selinux_ctx,
                      'permissions' : options.mode }

        print 'Path:            %s' % options.path
        print 'Directory:       %s' % options.directory
        print 'Owner:           %s' % file_info['owner']
        print 'Group:           %s' % file_info['group']
        print 'Mode:            %s' % file_info['permissions']
        print 'SELinux Context: %s' % file_info['selinux_ctx']

        # only add the revision field if the user supplied it
        if options.revision:
            file_info['revision'] = options.revision
            print 'Revision:        %i' % file_info['revision']

        if not options.directory:
            print
            print 'Contents'
            print '--------'
            print file_info['contents']

    if self.user_confirm():
        if options.symlink:
            self.client.configchannel.createOrUpdateSymlink(self.session,
                                                            options.channel,
                                                            options.path,
                                                            file_info)
        else:
            # compatibility for Satellite 5.3
            if not self.check_api_version('10.11'):
                del file_info['selinux_ctx']

                if file_info.has_key('revision'):
                    del file_info['revision']

            self.client.configchannel.createOrUpdatePath(self.session,
                                                         options.channel,
                                                         options.path,
                                                         options.directory,
                                                         file_info)

####################

def help_configchannel_updatefile(self):
    print 'configchannel_updatefile: Update a configuration file'
    print 'usage: configchannel_updatefile CHANNEL FILE'

def complete_configchannel_updatefile(self, text, line, beg, end):
    parts = line.split(' ')

    if len(parts) == 2:
        return tab_completer(self.do_configchannel_list('', True),
                                  text)
    elif len(parts) > 2:
        channel = parts[1]
        return tab_completer(self.do_configchannel_listfiles(channel, True),
                             text)

def do_configchannel_updatefile(self, args):
    (args, options) = parse_arguments(args)

    if len(args) != 2:
        self.help_configchannel_updatefile()
        return

    return self.do_configchannel_addfile(args[0], update_path = args[1])

####################

def help_configchannel_removefiles(self):
    print 'configchannel_removefile: Remove configuration files'
    print 'usage: configchannel_removefile CHANNEL <FILE ...>'

def complete_configchannel_removefiles(self, text, line, beg, end):
    parts = line.split(' ')

    if len(parts) == 2:
        return tab_completer(self.do_configchannel_list('', True),
                                  text)
    elif len(parts) > 2:
        channel = parts[1]
        return tab_completer(self.do_configchannel_listfiles(channel,
                                                                  True),
                                  text)

def do_configchannel_removefiles(self, args):
    (args, options) = parse_arguments(args)

    if len(args) < 2:
        self.help_configchannel_removefiles()
        return

    channel = args.pop(0)
    files = args

    if self.user_confirm('Remove these files [y/N]:'):
        self.client.configchannel.deleteFiles(self.session, channel, files)

# vim:ts=4:expandtab:
