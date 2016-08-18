require 'pathname'
require 'shellwords'
require 'shell'
WRANGLE_DIR = Pathname 'wrangle'
SCRIPTS_DIR = WRANGLE_DIR.join('scripts')

DIRS = {
    :fetched => WRANGLE_DIR.join('corral', 'fetched'),
    :homogenized => WRANGLE_DIR.join('corral', 'homogenized'),
    :published =>  Pathname('data'),
}

START_YEAR = 2003
END_YEAR = 2015 # data is updated on an annual basis, so this file
                # can be manually edited

FETCHED_DATAFILES = (START_YEAR..END_YEAR).map{|y| DIRS[:fetched].join("#{y}.csv") }
HOMOGENIZED_DATAFILES = FETCHED_DATAFILES.map{|p| DIRS[:homogenized].join(p.basename)}

desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        p.mkpath()
        puts "Created directory: #{p}"
    end
end


namespace :package do
    desc "Fetch all yearly CSV files."
    task :fetch do
        FETCHED_DATAFILES.each{|fn| Rake::Task[fn].invoke() }
    end

    desc "Homogenized the fetched yearly CSV files"
    task :homogenize do
        HOMOGENIZED_DATAFILES.each{|fn| Rake::Task[fn].invoke() }
    end
end


## File listing
HOMOGENIZED_DATAFILES.each do |destname|
    srcname = DIRS[:fetched].join(destname.basename)
    desc "#{destname.basename} CSV file with homogenized headers"
    file destname => srcname do
        cmdstr = ['python', SCRIPTS_DIR.join('homogenize.py'), srcname]
        Shell.new.system(Shellwords.join(cmdstr)) > destname.to_s
    end
end



FETCHED_DATAFILES.each do |yname|
    desc "#{yname.basename} text file as fetched and extracted from nyc.gov"
    file yname do
        year = yname.basename.to_s[/\d{4}/]
        cmdstr = ['bash', SCRIPTS_DIR.join('fetch_and_unpack.sh'), year]
        Shell.new.system(Shellwords.join(cmdstr)) > yname.to_s
    end
end





