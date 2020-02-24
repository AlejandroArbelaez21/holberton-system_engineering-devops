#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)([a-zA-z0-9.+-:]{0,9}+\b)/).join(",")
