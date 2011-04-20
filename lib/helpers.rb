require 'ipaddr'

class IpVersionDispatcher
  
  def dispatch (ip_address)
    
    # determine ip-version
    ip_version = nil
    ip_address_int = nil
    
    ip_helper = IPAddr.new(ip_address) rescue nil
    
    unless ip_helper.nil?
      puts "yai not nil"
      if (ip_helper.ipv6?)
        ip_version = :ipv6
      else
        ip_version = :ipv4
      end
      ip_address_int = ip_helper.to_i
    end
    
    yield ip_address_int, ip_version
  end
  
end